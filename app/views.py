from django.shortcuts import render
from django.contrib.auth.decorators import login_required

<<<<<<< HEAD
=======
@login_required
>>>>>>> 25c35da1111a0e159012650888808c7017ef0938
def home(request):
    return render(request, 'home.html')
