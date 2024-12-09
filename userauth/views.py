from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest, HttpResponseForbidden

import logging
logger = logging.getLogger(__name__)

ROLE_HOME_URLS = {
    'admin': 'admin:home',
    'doctor': 'doctor:home',
    'patient': 'patient:home',
}

VALID_ROLES = ['admin', 'doctor', 'patient']

@login_required
def home(request):
    """
    This view prevents logged-in users from accessing the home page.
    If a user is logged in, it redirects them based on their role.
    """
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
            
            if profile.role == 'doctor':
                return redirect('doctor:home')  # Doctor's home page
            elif profile.role == 'patient':
                return redirect('patient:home')  # Patient's home page
            else:
                return HttpResponseForbidden("You do not have permission to access this page.")
        except Profile.DoesNotExist:
            return render(request, 'userauth/no_profile.html')
    
    return render(request, 'userauth/index.html')



def register_view(request, role=None):
    form = RegisterForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        email = request.POST.get('email')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('app:home')

        user = User.objects.create_user(username=username, password=password, email=email)

        profile, created = Profile.objects.get_or_create(user=user)

        profile.role = role
        profile.save()

        if created:
            messages.success(request, f"Profile for {username} created with role: {role}")
        else:
            messages.success(request, f"Profile for {username} updated with new role: {role}")

        login(request, user)
        return redirect(ROLE_HOME_URLS.get(role, 'app:default_home'))

    return render(request, 'userauth/user/register.html', {"form": form, "role": role})


def login_user(request, role=None):
    logger.info(f"Attempting login for role: {role}")
    if role not in VALID_ROLES:
        return HttpResponseBadRequest("Invalid role specified.")

    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            try:
                profile = Profile.objects.get(user=user)
                if profile.role == role:
                    login(request, user)
                    return redirect(ROLE_HOME_URLS.get(role))
                else:
                    messages.error(request, "Role mismatch. Please log in with the correct role.")
            except Profile.DoesNotExist:
                messages.error(request, "No profile found. Please register.")
        else:
            messages.error(request, "Invalid username or password.")
        
        return redirect('userauth:login_user', role=role)

    return render(request, 'userauth/user/login.html', {'form': form, 'role': role})



def logout_user(request):
    logout(request)
    return redirect('app:home')
