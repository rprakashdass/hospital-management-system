from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Profile
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

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


from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import HttpResponseBadRequest
from .models import Profile

def register_view(request, role):
    if role not in ['admin', 'patient', 'doctor']:
        return HttpResponseBadRequest("Invalid role")
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            profile, created = Profile.objects.get_or_create(user=user)
            if created:
                profile.role = role
                profile.save()

            login(request, user)


            return redirect(f'{role}:home')
    else:
        form = RegisterForm()

    return render(request, 'user/register.html', {"form": form, "role": role})



def register_patient(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile, created = Profile.objects.get_or_create(user=user)
            if created:
                profile.role = 'patient'
                profile.save()
            login(request, user)
            return redirect('patient:home')
    else:
        form = RegisterForm()
    return render(request, 'user/register.html', {"form": form})

def login_user(request, role=None):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if role == 'patient':
                return redirect('patient:home')
            elif role == 'doctor':
                return redirect('doctor:home')
            else:
                return HttpResponse("Invalid role specified.")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login_user', role=role)

    return render(request, 'user/login.html', {'role': role})

def logout_user(request):
    logout(request)
    return redirect('app:home')
