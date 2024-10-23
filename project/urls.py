from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('app.urls')),
    path('userauth/', include('userauth.urls')),
    path('userauth/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
