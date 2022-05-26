from habit.models import Habit, User
from .serializers import HabitSerializer, UserSerializer

from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import authentication, permissions
# from rest_framework.decorators import api_view
# from rest_framework.reverse import reverse

# from habit.models import Habit, User
# from .serializers import HabitSerializer, UserSerializer
# from rest_framework.generics import (
#     CreateAPIView,
#     RetrieveAPIView,
#     UpdateAPIView,
#     DestroyAPIView)


# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'users': reverse('user-list-api', request=request, format=format),
#         'habits': reverse('habit-list-api', request=request, format=format)
#     })


# class UserListView(APIView):

#     def get(self, request, format=None):
#         """
#         Return a JSON list of all users
#         """
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)


# class HabitListView(APIView):

#     def get(self, request, format=None):
#         """
#         Return a JSON list of all habits
#         """
#         habits = Habit.objects.filter(user=request.user)
#         serializer = HabitSerializer(habits, many=True)
#         return Response(serializer.data)


# class HabitDetailView(RetrieveAPIView):
#     queryset = Habit.objects.all()
#     serializer_class = HabitSerializer


# class HabitCreateView(CreateAPIView):
#     queryset = Habit.objects.all()
#     serializer_class = HabitSerializer


# class HabitUpdateView(UpdateAPIView):
#     queryset = Habit.objects.all()
#     serializer_class = HabitSerializer


# class HabitDeleteView(DestroyAPIView):
#     queryset = Habit.objects.all()
#     serializer_class = HabitSerializer
