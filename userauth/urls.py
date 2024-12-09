from django.urls import path
from . import views

app_name = 'userauth'
urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('login/<str:role>/', views.login_user, name='login_user'),
    path('register/<str:role>/', views.register_view, name='register_user'),
]
