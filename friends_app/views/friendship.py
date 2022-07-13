from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.db.models import Q

from friends_app.models import Friendship


def friendship(request, action, pk):
    new_friend = get_object_or_404(User, pk=pk)

    if action == 'add':
        Friendship.objects.get_or_create(sender=request.user, receiver=new_friend)

    elif action == 'accept':
        friend = Friendship.objects.filter(Q(sender=pk) & Q(receiver=request.user.pk) & Q(waiting=True))[0]
        if friend:
            friend.waiting = False
            friend.friend = True
            friend.sub = True
            friend.save()
            return redirect('my_profile')

    elif action == 'reject':
        friend = Friendship.objects.filter(Q(sender=pk) & Q(receiver=request.user.pk) & Q(waiting=True))[0]

        if friend:
            friend.waiting = False
            friend.save()
            return redirect('profile')

    elif action == 'remove':
        friend = Friendship.objects.filter((Q(sender=pk) & Q(receiver=request.user.pk)) |
                                           (Q(sender=request.user.pk) & Q(receiver=pk)) & Q(friend=True))[0]

        if friend:
            friend.sender = new_friend
            friend.receiver = request.user
            friend.friend = False
            friend.sub = True
            friend.save()

    elif action == 'subscribe':
        Friendship.objects.get_or_create(sender=request.user, receiver=new_friend, waiting=False)

    elif action == 'unsubscribe':
        friend = Friendship.objects.filter(Q(sender=request.user.pk) & Q(receiver=pk) & Q(friend=False))
        friend.delete()

    return redirect(f'/profile/{pk}')