from django.contrib import admin
from .models import Enquiry

class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('user', 'prediction', 'created_at')  # Ensure 'created_at' exists in the model
    search_fields = ('user__username', 'prediction')  # Adjust based on your model
    list_filter = ('created_at',)  # Ensure 'created_at' exists and is a field

admin.site.register(Enquiry, EnquiryAdmin)
