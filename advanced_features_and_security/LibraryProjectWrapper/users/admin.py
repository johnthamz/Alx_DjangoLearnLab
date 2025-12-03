from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    
    # Add the custom fields to edit existing users
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    
    # Add the custom fields to the "add new user" form
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    
    # Display fields in the user list in admin
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_of_birth', 'profile_photo')
    
    # Optional: allow filtering by your custom fields
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'date_of_birth')

admin.site.register(CustomUser, CustomUserAdmin)

