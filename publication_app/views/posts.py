from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View

from publication_app.models import Post
from tags_app.models import Tag


class Posts(View):

    @staticmethod
    def get(request):
        users = []
        tags = Tag.objects.all()
        posts = Post.objects.filter(is_public=True)
        if posts:

            paginator = Paginator(posts, 3)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            context = {
                'title': "Посты",
                'name_text': 'Публикации друзей и фолловеров',
                'posts': posts,
                'tag': tags,
                'information': None,
                'page_obj': page_obj
            }

        else:
            context = {
                'title': "Посты",
                'information': 'У ваших друзей/фолловеров нет постов. Найдите новых пользователей, которые вам интересны'
            }

        return render(request, 'publication_app/news.html', context)