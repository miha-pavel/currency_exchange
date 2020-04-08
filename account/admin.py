from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


# Register your models here.
@admin.register(User)
class UserAdmin(UserAdmin):
    fields = ['email', 'username', 'phone', 'is_active', 'avatar']
    fieldsets = None
