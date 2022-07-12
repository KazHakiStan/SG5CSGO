from django.shortcuts import redirect

from publication_app.models import Post


def post_delete(request, pk):
    Post.objects.get(id=pk).delete()
    return redirect('posts')