from .views import UserViewSet, HabitViewSet, DateRecordViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'users', UserViewSet, 'users')
router.register(r'habits', HabitViewSet, 'habits')
router.register(r'habits/(?P<habit_pk>[^/.]+)/date_records', DateRecordViewSet, 'date_records')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
