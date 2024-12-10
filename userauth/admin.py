from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    # Display user-related info in the admin panel
    list_display = ('user', 'get_role_display', 'bio', 'birthdate')
    search_fields = ('user__username', 'bio', 'role')
    list_filter = ('role',)

# Register the Profile model to make it manageable via the Django Admin interface
admin.site.register(Profile, ProfileAdmin)
