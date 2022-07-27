from django.shortcuts import redirect

from comments_app.models import Comment


def comment_delete(request, pk):
    Comment.objects.get(id=pk).delete()
    return redirect('posts')