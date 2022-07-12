from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View

from publication_app.models import Post
from tags_app.models import Tag


class GetTag(View):

    @staticmethod
    def get(request, tag):

        our_tag = Tag.objects.filter(tag=tag)
        id_tag = None
        name_tag = None
        for i in our_tag:
            id_tag = i.pk
            name_tag = i.tag

        posts = Post.objects.filter(tag__id=id_tag)

        tags = Tag.objects.all()

        paginator = Paginator(posts, 3)

        page_number = request.GET.get('page')

        page_obj = paginator.get_page(page_number)

        context = {
            'title': 'Посты по тегам',
            'name_text': f'Публикации по тегу "{name_tag}"',
            'page_obj': page_obj,
            'tags': tags,
            'name_tag': name_tag,
        }
        return render(request, 'publication_app/news.html', context)