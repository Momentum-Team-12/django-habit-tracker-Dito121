from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from habit.models import Habit, User, DateRecord
from .serializers import HabitSerializer, UserSerializer, DateRecordSerializer
from rest_framework.generics import (
    ListCreateAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list-api', request=request, format=format),
        'habits': reverse('habit-list-api', request=request, format=format),
        'daterecords':reverse('date-records-list-api', request=request, format=format),
    })


class UserListView(APIView):

    def get(self, request, format=None):
        """
        Return a JSON list of all users
        """
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


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
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitUpdateView(UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitDeleteView(DestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class DateRecordView(APIView):

    def get(self, request, format=None):
        """
        Return a JSON list of all date records
        for all habits
        """
        date_records = DateRecord.objects.all()
        serializer = DateRecordSerializer(date_records, many=True)
        return Response(serializer.data)


class DateRecordListView(APIView):

    def get(self, request, pk, format=None):
        """
        Return a JSON list of all date records
        for a specific habit
        """
        habit = Habit.objects.filter(pk=pk)
        date_records = DateRecord.objects.filter(habit=habit[0])
        serializer = DateRecordSerializer(date_records, many=True)
        return Response(serializer.data)


class DateRecordDetailView(APIView):

    def get(self, request, habit_pk, daterecord_pk, format=None):
        """
        Return a JSON detail for a specific date record
        """
        habit = Habit.objects.filter(pk=habit_pk)
        date_records = DateRecord.objects.filter(habit=habit[0], pk=daterecord_pk)
        serializer = DateRecordSerializer(date_records, many=True)
        return Response(serializer.data)


class DateRecordCreateView(CreateAPIView):
    queryset = DateRecord.objects.all()
    serializer_class = DateRecordSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DateRecordUpdateView(UpdateAPIView):
    queryset = DateRecord.objects.all()
    serializer_class = DateRecordSerializer

    def get_object(self, daterecord_pk):
        queryset = self.get_queryset()

        obj = DateRecord.objects.filter()
        self.check_object_permissions(self.request, obj)
        return obj


class DateRecordDeleteView(DestroyAPIView):
    queryset = DateRecord.objects.all()
    serializer_class = DateRecordSerializer


# from habit.models import Habit, User
# from .serializers import HabitSerializer, UserSerializer

# from rest_framework import viewsets


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class HabitViewSet(viewsets.ModelViewSet):
#     queryset = Habit.objects.all()
#     serializer_class = HabitSerializer

#     def check_permissions(self, request):
#         """
#         Check if the request should be permitted.
#         Raises an appropriate exception if the request is not permitted.
#         """
#         for permission in self.get_permissions():
            
#             if not permission.has_permission(request, self):
#                 self.permission_denied(
#                     request,
#                     message=getattr(permission, 'message', None),
#                     code=getattr(permission, 'code', None)
#                 )
