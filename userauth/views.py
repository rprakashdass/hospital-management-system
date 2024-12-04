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

# Mapping roles to their respective home views
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
                return HttpResponseForbidden("You do not have permission to access this page.")  # Access denied if the role is unknown
        except Profile.DoesNotExist:
            return render(request, 'no_profile.html')
    
    # If not logged in, return the regular home page
    return render(request, 'index.html')



def register_view(request, role=None):
    form = RegisterForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('app:home')

        # Create the user object
        user = User.objects.create_user(username=username, password=password)
        
        # Check if a profile already exists
        try:
            profile = Profile.objects.get(user=user)
            profile.role = role  # Update the role in the Profile model
            profile.save()
            messages.success(request, f"Profile for {username} updated with role: {role}")
            
            login(request, user)
            return redirect(ROLE_HOME_URLS[role])

        except Profile.DoesNotExist:
            # Create a new profile if it doesn't exist
            profile = Profile.objects.create(user=user, role=role)
            profile.save()
            messages.success(request, f"Profile for {username} created with role: {role}")
            
            login(request, user)
            return redirect(ROLE_HOME_URLS[role])
    else:
        form = RegisterForm()

    return render(request, 'user/register.html', {"form": form, "role": role})


def login_user(request, role=None):
    form = LoginForm()
    # Check if the role is valid
    if role not in ROLE_HOME_URLS:
        return HttpResponseBadRequest("Invalid role specified.")

    # Handle POST request for login
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            try:
                # Check if the user has a profile
                profile = Profile.objects.get(user=user)
                
                if profile.role == role:
                    # Role matches, redirect to the correct home page
                    return redirect(ROLE_HOME_URLS.get(role, 'userauth:login_user'))
                else:
                    # Role doesn't match, notify the user
                    messages.error(request, "Role mismatch. Please ensure you are logging in with the correct credentials.")
                    return redirect('userauth:login_user', role=role)
            
            except Profile.DoesNotExist:
                # If no profile exists, ask the user to complete their profile
                messages.error(request, "Profile not found. Please complete your profile first.")
                return redirect('userauth:register', role=role)
        else:
            # If the user doesn't exist, notify the user about invalid credentials
            messages.error(request, "Invalid username or password.")
            return redirect('userauth:login_user', role=role)
    else:
        # Display the login form
        form = LoginForm()

    return render(request, 'user/login.html', {'form': form, 'role': role})


def logout_user(request):
    logout(request)
    return redirect('app:home')
