from django.urls import path
from api import views as api_views


urlpatterns = [
    path('', api_views.api_root),
    path('users', api_views.UserListView.as_view(), name='user-list-api'),
    path('habits', api_views.HabitListView.as_view(), name='habit-list-api'),

    path('habit/create/', api_views.HabitCreateView.as_view(), name='habit-create-api'),
    path('habit/<int:pk>/', api_views.HabitDetailView.as_view(), name='habit-detail-api'),
    path('habit/<int:pk>/update/', api_views.HabitUpdateView.as_view(), name='habit-update-api'),
    path('habit/<int:pk>/delete/', api_views.HabitDeleteView.as_view(), name='habit-delete-api'),
]
