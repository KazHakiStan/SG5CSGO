from django.urls import path

from tags_app.views.get_tag import GetTag
from tags_app.views.tags import Tags

urlpatterns = [
    path('tags/', Tags.as_view(), name='tags'),
    path('tag/<str:tag>/', GetTag.as_view(), name='tag'),
]