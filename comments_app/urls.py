from django.contrib.auth.decorators import login_required
from django.urls import path

from comments_app.views.comment_del import comment_delete

urlpatterns = [
    path('comment_del/<int:pk>', login_required(comment_delete), name='comment_del'),
]
