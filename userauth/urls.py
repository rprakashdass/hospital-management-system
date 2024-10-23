from django.urls import path
from . import views

app_name = 'userauth'

urlpatterns = [
    path('', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
]
