from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from habit.models import Habit, User, DateRecord
from .serializers import (
    UserSerializerForAdmin,
    HabitListSerializerForUser,
    HabitDetailSerializerForUser,
    HabitListSerializerForAdmin,
    HabitDetailSerializerForAdmin,
    DateRecordSerializerForUser,
    DateRecordSerializerForAdmin)
from rest_framework import viewsets
from django.db.models.query import QuerySet


@api_view(['GET'])
def api_root(request, format=None):
    if request.user.is_superuser:
        return Response({
            'users': reverse('user-list-api', request=request, format=format),
            'habits': reverse('habit-list-api', request=request, format=format),
        })
    else:
        return Response({
            'habits': reverse('habit-list-api', request=request, format=format),
        })


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializerForAdmin
    permission_classes = (IsAdminUser,)


class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitListSerializerForUser
    permission_classes = (IsAuthenticated,)

    serializer_action_classes = [
        {'list': HabitListSerializerForUser,
            'create': HabitListSerializerForUser,
            'retrieve': HabitDetailSerializerForUser,
            'update': HabitListSerializerForUser,
            'partial_update': HabitListSerializerForUser,
            'destroy': HabitListSerializerForUser},
        {'list': HabitListSerializerForAdmin,
            'create': HabitListSerializerForAdmin,
            'retrieve': HabitDetailSerializerForAdmin,
            'update': HabitListSerializerForAdmin,
            'partial_update': HabitListSerializerForAdmin,
            'destroy': HabitListSerializerForAdmin}
    ]

    def get_serializer_class(self, *args, **kwargs):
        """Instantiate the list of serializers per action from class attribute (must be defined)."""
        kwargs['partial'] = True
        try:
            if self.request.user.is_superuser:
                return self.serializer_action_classes[1][self.action]
            else:
                return self.serializer_action_classes[0][self.action]
        except (KeyError, AttributeError):
            return super(HabitViewSet, self).get_serializer_class()

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
        if self.request.user.is_superuser:
            serializer.save()

        else:
            serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        user = self.request.user._wrapped if hasattr(self.request.user, '_wrapped') else self.request.user
        if user == instance.user or user.is_superuser:
            instance.delete()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class DateRecordViewSet(viewsets.ModelViewSet):
    queryset = DateRecord.objects.all()
    serializer_class = DateRecordSerializerForUser
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, pk):
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method."
            % self.__class__.__name__
        )

        queryset = self.queryset
        if isinstance(queryset, QuerySet) and not self.request.user.is_superuser:
            queryset = queryset.filter(habit=self.request.user)

        return queryset

    def get_serializer_class(self):
        """
        Return the class to use for the serializer.
        Defaults to using `self.serializer_class`.

        You may want to override this if you need to provide different
        serializations depending on the incoming request.

        (Eg. admins get full serialization, others get basic serialization)
        """
        assert self.serializer_class is not None, (
            "'%s' should either include a `serializer_class` attribute, "
            "or override the `get_serializer_class()` method."
            % self.__class__.__name__
        )

        if not self.request.user.is_superuser:
            return self.serializer_class

        return DateRecordSerializerForAdmin

    def perform_create(self, serializer):
        if not self.request.user.is_superuser:
            serializer.save(user=self.request.user)

        else:
            serializer.save()

    def perform_update(self, serializer):
        if not self.request.user.is_superuser and str(self.request.user.pk) == self.request.data['user']:
            serializer.save(user=self.request.user)

        elif self.request.user.is_superuser:
            serializer.save()

    def perform_destroy(self, instance):
        if self.request.user == instance.user or self.request.user.is_superuser:
            instance.delete()
