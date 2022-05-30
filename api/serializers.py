from rest_framework import serializers
from habit.models import Habit, User, DateRecord


class UserSerializerForAdmin(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'password',
            'habits',
        )


class HabitSerializerForUser(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = (
            'id',
            'name',
            'target',
            'unit',
            'frequency',
            'created_at',
            'starts_on',
            'ends_on',
        )


class HabitSerializerForAdmin(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = (
            'user',
            'id',
            'name',
            'target',
            'unit',
            'frequency',
            'created_at',
            'starts_on',
            'ends_on',
        )


class DateRecordSerializerForUser(serializers.ModelSerializer):
    class Meta:
        model = DateRecord
        fields = (
            'id',
            'habit',
            'created_at',
            'date',
            'actual',
        )


class DateRecordSerializerForAdmin(serializers.ModelSerializer):
    class Meta:
        model = DateRecord
        fields = (
            'id',
            'habit',
            'created_at',
            'date',
            'actual',
        )
