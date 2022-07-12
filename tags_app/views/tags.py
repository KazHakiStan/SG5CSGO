from django.db.models import Count
from django.shortcuts import render
from django.views import View

from tags_app.models import Tag


class Tags(View):
    @staticmethod
    def get(request):
        count_tag = Tag.objects.annotate(cnt=Count('tag_post')).order_by('-cnt')

        context = {
            'title': 'Область тегов',
            'tags': count_tag,
        }
        return render(request, 'tags_app/tags.html', context)