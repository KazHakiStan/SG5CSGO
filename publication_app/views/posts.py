from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from django.views import View

from comments_app.forms.new_comment import AddCommentsForm
from friends_app.models import Friendship
from publication_app.models import Post
from tags_app.models import Tag


class Posts(View):

    @staticmethod
    def get(request):
        friendship = Friendship.objects.filter(Q(sender=request.user.pk) |
                                               (Q(receiver=request.user.pk) & Q(friend=True)))
        form = AddCommentsForm()
        users = []

        for friend in friendship:

            if friend.sender.pk not in users:
                users.append(friend.sender.pk)

            if friend.receiver.pk not in users:
                users.append(friend.receiver.pk)

        if friendship:
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
                    'page_obj': page_obj,
                    'form': form
                }

            else:
                context = {
                    'title': "Посты",
                    'information': 'У ваших друзей/фолловеров нет постов. Найдите новых пользователей, которые вам интересны'
                }
        else:
            context = {
                'title': "Посты",
                'information': 'Вы еще никого не добавили в друзья/фолловеры. '
                               'Найдите пользователей, которые вам интересны'
            }

        return render(request, 'publication_app/news.html', context)