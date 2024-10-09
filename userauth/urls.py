from django.urls import path
from userauth import views

app_name = 'userauth'

urlpatterns = [
    path('', views.home, name='home'),
]
