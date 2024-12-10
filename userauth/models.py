from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    # Define the role choices
    USER_ROLES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
        ('admin', 'Admin'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    role = models.CharField(max_length=10, choices=USER_ROLES, default='doctor')
    
    bio = models.TextField(blank=True, null=True)
    birthdate = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"
