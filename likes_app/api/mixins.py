from rest_framework.decorators import action
from rest_framework.response import Response
from .. import views
from .serializers import FanSerializer


class LikedMixin:
    @action(detail=True, methods=['POST'])
    def like(self, request, pk=None):
        """Лайкает `obj`.
        """
        obj = self.get_object()
        views.add_like(obj, request.user)
        return Response()

    @action(detail=True, methods=['POST'])
    def unlike(self, request, pk=None):
        """Удаляет лайк с `obj`.
        """
        obj = self.get_object()
        views.remove_like(obj, request.user)
        return Response()

    @action(detail=True, methods=['POST'])
    def fans(self, request, pk=None):
        """Получает всех пользователей, которые лайкнули `obj`.
        """
        obj = self.get_object()
        fans = views.get_fans(obj)
        serializer = FanSerializer(fans, many=True)
        return Response(serializer.data)