from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse

from publication_app.models import Post
from .models import Like

User = get_user_model()


def add_like(request, pk):
    """Лайкает `obj`.
    """
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('posts'))


def remove_like(request, pk):
    """Удаляет лайк с `obj`.
    """
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.delete(request.user)
    return HttpResponseRedirect(reverse('posts'))


def is_fan(request, pk) -> bool:
    """Проверяет, лайкнул ли `user` `obj`.
    """
    if not request.user.is_authenticated:
        return False
    likes = Post.objects.likes.filter(pk=pk)

    return likes.exists()


def get_fans(obj):
    """Получает всех пользователей, которые лайкнули `obj`.
    """
    obj_type = ContentType.objects.get_for_model(obj)
    return User.objects.filter(
        likes__content_type=obj_type, likes__object_id=obj.id)