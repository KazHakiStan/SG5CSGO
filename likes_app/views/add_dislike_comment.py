from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View

from comments_app.models import Comment
from publication_app.models import Post


class AddDislikeComment(LoginRequiredMixin, View):

    def post(self, request, pk, *args, **kwargs):

        comment = Comment.objects.get(pk=pk)

        is_like_c = False

        for like in comment.likes.all():
            if like == request.user:
                is_like_c = True
                break

        if is_like_c:
            comment.likes.remove(request.user)

        is_dislike_c = False

        for dislike in comment.dislikes.all():
            if dislike == request.user:
                is_dislike_c = True
                break

        if not is_dislike_c:
            comment.dislikes.add(request.user)

        if is_dislike_c:
            comment.dislikes.remove(request.user)

        return HttpResponseRedirect(reverse('post', args=[str(comment.post_id)]))
