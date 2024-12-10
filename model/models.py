from django.db import models
from django.contrib.auth.models import User

class Enquiry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enquiries')  # Link to User model
    height = models.FloatField()
    weight = models.FloatField()
    temperature = models.FloatField()
    heart_rate = models.FloatField()
    cholestrol = models.FloatField()
    blood_sugar = models.FloatField()
    systolic = models.FloatField()
    diastolic = models.FloatField()
    existing_conditions = models.CharField(max_length=100)
    family_history = models.CharField(max_length=3)
    smoking_status = models.CharField(max_length=7)
    lab_status = models.CharField(max_length=50)
    symptom = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    prediction = models.CharField(max_length=100, null=True, blank=True)  # New field for the prediction result

    def __str__(self):
        return f"Enquiry from {self.user.username} - {self.height}cm, {self.weight}kg"

    class Meta:
        db_table = 'enquiries'
