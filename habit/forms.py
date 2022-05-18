from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Habit, DateRecord
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = [
            'name',
            'target',
            'unit',
            'frequency',
            'starts_on',
            'ends_on',
        ]

class DateRecordForm(forms.ModelForm):
    class Meta:
        model = DateRecord
        fields = [
            'habit',
            'actual',
            'date',
        ]
