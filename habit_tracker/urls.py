"""habit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from habit import views as habit_views

urlpatterns = [
    path("", habit_views.list_habits, name='list_habits'),
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('accounts/', include('registration.backends.simple.urls')),
    path("habit/<int:pk>", habit_views.habit_details, name="habit_details"),
    path("habit/new", habit_views.add_habit, name="add_habit"),
    path("habit/<int:pk>/edit", habit_views.edit_habit, name="edit_habit"),
    path("habit/<int:pk>/delete", habit_views.delete_habit, name="delete_habit"),
    path("habit/<int:pk>/date_record/new", habit_views.add_date_record, name="add_date_record"),
    path("habit/date_record/<int:pk>/edit", habit_views.edit_date_record, name="edit_date_record"),
    path("habit/date_record/<int:pk>/delete", habit_views.delete_date_record, name="delete_date_record"),
    path("accounts/login/", habit_views.list_habits, name="login"),
    path("accounts/logout/", habit_views.logout, name="logout"),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls')),
]
