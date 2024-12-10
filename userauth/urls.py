from django.urls import path
from . import views

app_name = 'userauth'

urlpatterns = [
    path('login/', views.login_view, name='login_user'),
    path('register/', views.register_view, name='register_user'),
    path('logout/', views.logout_view, name='logout'),
]