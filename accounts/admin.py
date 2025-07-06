from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Register the custom User model in the admin.
    """
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('vinted_username', 'vinted_password')}),
    )