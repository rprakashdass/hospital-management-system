from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('', include('app.urls')),
    path('', include('userauth.urls')),
    path('', include('django.contrib.auth.urls')),
    path('d/', include('doctor.urls')),
    path('admin/', admin.site.urls),
]
