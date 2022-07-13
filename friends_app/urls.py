from django.contrib.auth.decorators import login_required
from django.urls import path

from friends_app.views.friendship import friendship

urlpatterns = [
    path('connect/<str:action>/<int:pk>', login_required(friendship), name='friendship'),
]