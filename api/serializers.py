from rest_framework import serializers
from habit.models import Habit

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
