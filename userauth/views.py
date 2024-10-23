from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Profile
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    try:
        profile = Profile.objects.get(user=request.user)
        if profile.role == 'doctor':
            return redirect('register')
        else:
            return redirect('register')
    except Profile.DoesNotExist:
        return render(request, 'no_profile.html') 

def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile, created = Profile.objects.get_or_create(user=user)
            if created:
                profile.role = 'doctor'
                profile.save()
            login(request, user)
            return redirect('doctor:home')
    else:
        form = RegisterForm()
    return render(request, 'user/register.html', {"form": form})


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('doctor:home')
        else:
            messages.success(request, "Login with correct credentials")
            return redirect('login')
    return render(request, 'user/login.html', {messages:messages})

def logout_user(request):
    logout(request)
    return redirect('login')