from rest_framework import filters
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from publication_app.api.serializers.posts import PostSerializer
from publication_app.models import Post


class PostsView(GenericViewSet, ListModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(is_public=True)
    filter_backends = [filters.OrderingFilter]
    ordering_filters = ['-created_at']