from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View

from comments_app.models import Comment
from publication_app.models import Post


class AddLike(LoginRequiredMixin, View):

    def post(self, request, pk, *args, **kwargs):

        post = Post.objects.get(pk=pk)

        is_dislike_p = False

        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike_p = True
                break

        if is_dislike_p:
            post.dislikes.remove(request.user)

        is_like_p = False

        for like in post.likes.all():
            if like == request.user:
                is_like_p = True
                break

        if not is_like_p:
            post.likes.add(request.user)

        if is_like_p:
            post.likes.remove(request.user)


        return HttpResponseRedirect(reverse('post', args=[str(pk)]))
