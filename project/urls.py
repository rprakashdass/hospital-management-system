from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Default path for the app
    path('', include('app.urls')),  # Make sure app.urls exists and handles the default homepage or main views

    # User authentication-related paths
    path('u/', include('userauth.urls')),  # Custom userauth URLs
    path('u/auth/', include('django.contrib.auth.urls')),  # Include the default Django auth URLs under a different path

    # Doctor-related paths
    path('d/', include('doctor.urls')),

    # Patient-related paths
    path('p/', include('patient.urls')),

    # Model-related paths (ensure this is correct)
    path('lehme/', include('model.urls')),

    # Django admin path
    path('admin/', admin.site.urls),
]
