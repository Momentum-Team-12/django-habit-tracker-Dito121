from rest_framework import serializers
from habit.models import Habit, User


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = (
            'id',
            'target',
            'user',
            'unit',
            'frequency',
            'created_at',
            'starts_on',
            'ends_on',
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
        )
