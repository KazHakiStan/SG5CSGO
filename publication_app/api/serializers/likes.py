from rest_framework import serializers

from publication_app.models import Post


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = 'likes'
