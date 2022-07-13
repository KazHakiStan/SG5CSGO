from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from friends_app.models import Friendship


class ProfileUserView(View):
    @staticmethod
    def get(request, pk):
        users = get_object_or_404(User, pk=pk)

        if users.pk == request.user.pk:
            return redirect('profile')

        friend = Friendship.objects.filter(Q(sender=pk) | Q(receiver=pk)).filter(friend=True)
        sub = Friendship.objects.filter(sender=pk, sub=True)

        is_friendship = Friendship.objects.filter((Q(sender=pk) & Q(receiver=request.user.pk)) |
                                                  (Q(sender=request.user.pk) & Q(receiver=pk)))

        is_friend = None
        is_subscribed = None
        is_following = None

        if is_friendship.filter(friend=True):
            is_friend = True

        elif is_friendship.filter(Q(sender=request.user.pk) & Q(sub=True)):
            is_following = True

        elif is_friendship.filter(Q(receiver=request.user.pk) & Q(sub=True)):
            is_subscribed = True

        context = {
            'title': f'Профиль {users.username}',
            'users': users,
            'friends': friend,
            'subs': sub,
            'is_friend': is_friend,
            'is_subscribed': is_subscribed,
            'is_following': is_following,
        }
        return render(request, 'profile_app/profile.html', context)