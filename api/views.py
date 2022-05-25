from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from habit.models import Habit
from .serializers import HabitSerializer
from rest_framework.generics import CreateAPIView, RetrieveAPIView


class HabitListView(APIView):

    def get(self, request, format=None):
        """
        Return a JSON list of all habits
        """
        habits = Habit.objects.filter(user=request.user)
        serializer = HabitSerializer(habits, many=True)
        return Response(serializer.data)


class HabitDetailView(RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitCreateView(CreateAPIView):
    pass
