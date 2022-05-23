from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import UniqueConstraint


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username} pk={self.pk}>"

    def __str__(self):
        return self.username


class Habit(models.Model):
    name = models.CharField(max_length=255)
    target = models.IntegerField()
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='habits', max_length=255)
    unit = models.CharField(max_length=255)
    frequency = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    starts_on = models.DateField()
    ends_on = models.DateField()

    def __str__(self):
        return self.name


class DateRecord(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    habit = models.ForeignKey('Habit', on_delete=models.CASCADE, related_name='date_records', max_length=255)
    actual = models.IntegerField()
    date = models.DateField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['habit', 'date'], name='unique_date_record')
        ]

    def __str__(self):
        return str(self.date)
