from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('', include('app.urls')),
<<<<<<< HEAD
    path('', include('app.urls')),
    path('u/', include('userauth.urls')),
    path('u/', include('django.contrib.auth.urls')),
    path('d/', include('doctor.urls')),
    path('p/', include('patient.urls')),
=======
    path('', include('userauth.urls')),
    path('', include('django.contrib.auth.urls')),
    path('d/', include('doctor.urls')),
>>>>>>> 25c35da1111a0e159012650888808c7017ef0938
    path('admin/', admin.site.urls),
]
