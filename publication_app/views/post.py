from django.shortcuts import render
from django.views import View

from publication_app.models import Post


class PostView(View):
    @staticmethod
    def get(request, pk):
        posts = Post.objects.get(pk=pk)

        context = {
            'title': 'Пост',
            'name_text': 'Публикации',
            'posts': posts,
        }
        return render(request, 'publication_app/post.html', context)