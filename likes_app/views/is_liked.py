
from publication_app.models import Post


def is_fan(request, pk) -> bool:
    """Проверяет, лайкнул ли `user` `obj`.
    """
    if not request.user.is_authenticated:
        return False
    likes = Post.objects.likes.filter(pk=pk)

    return likes.exists()