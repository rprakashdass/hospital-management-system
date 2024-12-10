from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm
from .models import Profile
from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

import logging
logger = logging.getLogger(__name__)

@login_required
def home(request):
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
            return redirect('app:home')
        except Profile.DoesNotExist:
            return render(request, 'userauth/no_profile.html')
    return render(request, 'userauth/index.html')


def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            role = form.cleaned_data['role']

            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists!")
                return redirect('userauth:register_user')

            user = User.objects.create_user(username=username, password=password, email=email)

            profile, created = Profile.objects.get_or_create(user=user, role=role)
            profile.role = role
            profile.save()

            messages.success(request, f"Profile for {username} is created and role is {role}")
            login(request, user)
           
            if role == 'doctor':
                return redirect('doctor:home')
            else:
                return redirect('patient:home')
        

    return render(request, 'userauth/register.html', {"form": form})


def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        role = form.cleaned_data.get('role')

        user = authenticate(request, username=username, password=password)
        if user:
            try:
                profile = Profile.objects.get(user=user)
                if profile.role == role:
                    login(request, user)
                    # messages.success(request, f"Welcome {username}!")
                    return redirect('doctor:home')
                else:
                    messages.error(request, f"Role mismatch. You are not registered as a {role}.")
            except Profile.DoesNotExist:
                messages.error(request, "Profile not found for this user.")
        else:
            messages.error(request, "Invalid username or password.")
        
        return redirect('userauth:login_user')

    return render(request, 'userauth/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('userauth:register_user')
