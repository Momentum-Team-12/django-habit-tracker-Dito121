from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)

    def __str__(self):
        return self.username


class Habit(models.Model):
    name = models.CharField(max_length=255)
    target = models.CharField(max_length=255)
    custom_user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='habits', max_length=255)
    unit = models.CharField(max_length=255)
    frequency = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    ends_on = models.DateField()


class DATERECORD(models.Model):
    habit = models.ForeignKey('Habit', on_delete=models.CASCADE, related_name='daterecords', max_length=255)
    actual = models.IntegerField()
