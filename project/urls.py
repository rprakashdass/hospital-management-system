from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('', include('app.urls')),
    path('', include('app.urls')),
    path('u/', include('userauth.urls')),
    path('u/', include('django.contrib.auth.urls')),
    path('d/', include('doctor.urls')),
    path('p/', include('patient.urls')),
    path('lehme/', include('model.urls')),
    path('admin/', admin.site.urls),
]
