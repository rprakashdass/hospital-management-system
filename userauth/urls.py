from django.urls import path
from . import views

app_name = 'userauth'
urlpatterns = [
    path('register/<str:role>/', views.register_view, name='register'),
    path('login/<str:role>/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout'),
    path('', views.home, name='home'),
]
