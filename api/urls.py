from django.urls import path
from api import views as api_views


urlpatterns = [
    path('', api_views.api_root),
    path('users/', api_views.UserListView.as_view(), name='user-list-api'),
    path('habits/', api_views.HabitListView.as_view(), name='habit-list-api'),
    path('habit/<int:pk>/daterecords/', api_views.DateRecordListView.as_view(), name='date-record-list-api'),

    path('habit/create/', api_views.HabitCreateView.as_view(), name='habit-create-api'),
    path('habit/<int:pk>/', api_views.HabitDetailView.as_view(), name='habit-detail-api'),
    path('habit/<int:pk>/update/', api_views.HabitUpdateView.as_view(), name='habit-update-api'),
    path('habit/<int:pk>/delete/', api_views.HabitDeleteView.as_view(), name='habit-delete-api'),

    path('habit/<int:pk>/daterecord/create/', api_views.DateRecordCreateView.as_view(), name='date-record-create-api'),
    path('habit/<int:habit_pk>/daterecord/<int:daterecord_pk>/', api_views.DateRecordDetailView.as_view(), name='date-record-detail-api'),
    path('habit/<int:habit_pk>/daterecord/<int:daterecord_pk>/update/', api_views.DateRecordUpdateView.as_view(), name='date-record-update-api'),
    path('habit/<int:habit_pk>/daterecord/<int:daterecord_pk>/delete/', api_views.DateRecordDeleteView.as_view(), name='date-record-delete-api'),
]


# from .views import HabitViewSet, UserViewSet
# from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register(r'habits', HabitViewSet, 'habits')
# router.register(r'users', UserViewSet, 'users')
# urlpatterns = router.urls
