from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from publication_app.models import Post
from tags_app.models import Tag


class GetTag(ListView):
    queryset = Post.objects.all()
    template_name = 'publication_app/news.html'
    paginate_by = 3
    context_object_name = 'posts'

    def get_queryset(self):
        self.queryset.filter(tag__tag=self.kwargs['tag'])
        return self.queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['title'] = f'Посты по тегу {self.kwargs["tag"]}'
        context['name_text'] = context['title']
        context['tags'] = Tag.objects.all()
        context['name_tag'] = self.kwargs['tag']

        return context

    # @staticmethod
    # def get(request, tag):
    #
    #     our_tag = Tag.objects.filter(tag=tag)
    #
    #     posts = Post.objects.filter(tag=our_tag)
    #
    #     tags = Tag.objects.all()
    #
    #     paginator = Paginator(posts, 3)
    #
    #     page_number = request.GET.get('page')
    #
    #     page_obj = paginator.get_page(page_number)
    #
    #     context = {
    #         'title': 'Посты по тегам',
    #         'name_text': f'Публикации по тегу "{our_tag}"',
    #         'page_obj': page_obj,
    #         'tags': tags,
    #         'name_tag': our_tag,
    #     }
    #     return render(request, 'publication_app/news.html', context)