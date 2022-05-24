from django.urls import path
from api import views as api_views

urlpatterns = [
    path('habits', api_views.HabitListView.as_view(), name='habit-list-api')
]
