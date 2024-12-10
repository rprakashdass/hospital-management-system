from django.urls import path
from . import views

app_name = "lehme"

urlpatterns = [
    path('', views.home, name='home'),
    path('predict/', views.predict_disease, name='predict'),
]
