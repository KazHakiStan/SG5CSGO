from rest_framework import serializers
from ..models import Post
from likes_app import views as likes_services


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'total_likes'
            'is_fan',
        )

    def get_is_fan(self, obj) -> bool:
        user = self.context.get('request').user
        return likes_services.is_fan(obj, user)