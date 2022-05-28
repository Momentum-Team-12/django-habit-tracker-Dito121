from rest_framework import serializers
from habit.models import Habit, User, DateRecord


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'habits',
        )


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
            'date_records',
        )


class DateRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateRecord
        fields = (
            'id',
            'created_at',
            'date',
            'actual',
            'habit',
        )
