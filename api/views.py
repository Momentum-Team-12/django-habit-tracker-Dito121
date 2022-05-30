from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from habit.models import Habit, User, DateRecord
from .serializers import (
    UserSerializerForAdmin,
    HabitSerializerForUser,
    HabitSerializerForAdmin,
    DateRecordSerializerForUser,
    DateRecordSerializerForAdmin)
from rest_framework import viewsets
from django.db.models.query import QuerySet


@api_view(['GET'])
def api_root(request, format=None):
    if request.user.is_authenticated():
        return Response({
            'habits': reverse('habit-list-api', request=request, format=format),
            'date_records': reverse('date-records-list-api', request=request, format=format),
        })
    elif request.user.is_admin():
        return Response({
            'users': reverse('user-list-api', request=request, format=format),
            'habits': reverse('habit-list-api', request=request, format=format),
            'date_records': reverse('date-records-list-api', request=request, format=format),
        })


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializerForAdmin
    permission_classes = (IsAdminUser,)


class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializerForUser
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method."
            % self.__class__.__name__
        )

        queryset = self.queryset
        if isinstance(queryset, QuerySet) and not self.request.user.is_superuser:
            queryset = queryset.filter(user=self.request.user)

        return queryset



    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        if str(self.request.user.pk) == self.request.data['user']:
            serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        if self.request.user == instance.user:
            instance.delete()


class DateRecordViewSet(viewsets.ModelViewSet):
    queryset = DateRecord.objects.all()
    serializer_class = DateRecordSerializerForUser
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method."
            % self.__class__.__name__
        )

        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            queryset = queryset.filter(id=self.request.user.id)

        return queryset

    def perform_create(self, serializer):
        serializer.save()
