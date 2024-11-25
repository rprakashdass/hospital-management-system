from . import views
from django.urls import path

app_name = "lehme"
urlpatterns = [
    path('', views.home, name="home"),
    path('predict/', views.predict_disease, name="predict")
]
