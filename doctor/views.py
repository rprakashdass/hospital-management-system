from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from userauth.models import Profile

@login_required
def home(request):
    try:
        # user's profile
        profile = Profile.objects.get(user=request.user)
        
        if profile.role == 'doctor':
            return render(request, 'doctor/home.html')
        else:
            return render(request, 'doctor/home.html')
            # return HttpResponseForbidden("You do not have access to this page.")  # 403 error page
    except Profile.DoesNotExist:
        return HttpResponseForbidden("Profile not found or invalid user.")
