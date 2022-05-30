from .views import UserViewSet, HabitViewSet, DateRecordViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'users', UserViewSet, 'users')
router.register(r'habits', HabitViewSet, 'habits')
router.register(r'habit/(?P<habit_pk>[^/.]+)/date_records', DateRecordViewSet, 'date_records')
urlpatterns = router.urls
