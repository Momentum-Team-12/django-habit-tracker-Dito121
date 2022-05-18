from django.contrib.auth.models import AbstractUser
from django.db import models


class Meta:
    db_table = 'date_record'
    constraints = [
        models.UniqueConstraint(fields=['habit', 'date'], name='unique_date_record')
    ]


class CustomUser(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Habit(models.Model):
    name = models.CharField(max_length=255)
    target = models.IntegerField()
    custom_user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='habits', max_length=255)
    unit = models.CharField(max_length=255)
    frequency = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    starts_on = models.DateField(null=True, blank=True)
    ends_on = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class DateRecord(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    habit = models.ForeignKey('Habit', on_delete=models.CASCADE, related_name='date_records', max_length=255)
    actual = models.IntegerField()
    date = models.DateField()
