from django.contrib.auth.models import User
from rest_framework import filters
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from publication_app.api.serializers.likes import LikeSerializer
from publication_app.models import Post


class LikesView(GenericViewSet, ListModelMixin):
    serializer_class = LikeSerializer
    queryset = User.objects.filter()
    filter_backends = [filters.OrderingFilter]
    ordering_filters = ['-created_at']