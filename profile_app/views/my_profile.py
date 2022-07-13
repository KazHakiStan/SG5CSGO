from django.db.models import Q
from django.shortcuts import render
from django.views import View

from friends_app.models import Friendship
from publication_app.models import Post


class Profile(View):

    @staticmethod
    def get(request):
        post = Post.objects.filter(user=request.user.pk)

        friend = Friendship.objects.filter(Q(sender=request.user.pk) | Q(receiver=request.user.pk)). \
            filter(friend=True)

        sub = Friendship.objects.filter(sender=request.user.pk, sub=True)

        waiting = Friendship.objects.filter(receiver=request.user.pk, waiting=True)

        context = {
            'title': 'Информация о вашем аккаунте',
            'posts': post,
            'friends': friend,
            'subs': sub,
            'waiting': waiting,
        }

        return render(request, 'profile_app/my_profile.html', context)
