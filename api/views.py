from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from habit.models import Habit
from .serializers import HabitSerializer


class HabitListView(APIView):

    def get(self, request, format=None):
        """
        Return a JSON list of all habits
        """
        habits = Habit.objects.filter(user=request.user)
        serializer = HabitSerializer(habits, many=True)
        return Response(serializer.data)
