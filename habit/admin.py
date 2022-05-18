from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Habit, DateRecord


admin.site.register(CustomUser)
admin.site.register(Habit)
admin.site.register(DateRecord)
