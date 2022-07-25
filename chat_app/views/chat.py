from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User

from friends_app.models import Friendship
from ..models import Chat
from ..forms.chat_form import ChatForm


class ChatView(View):

    @staticmethod
    def get(request, pk):
        friend = Friendship.objects.filter(Q(sender=request.user.pk) | Q(receiver=request.user.pk)). \
            filter(friend=True)
        chat_friend = User.objects.get(pk=pk)
        message = Chat.objects.filter(
            (Q(sender=pk) & Q(receiver=request.user.pk)) |
            (Q(sender=request.user.pk) & Q(receiver=pk))
        ).order_by("pk")

        form = ChatForm()
        context = {
            'title': f'Чат с пользователем ',
            'message': message,
            'form': form,
            'friends': friend,
            'chat_friend': chat_friend
        }
        return render(request, 'chat_app/chat.html', context)

    @staticmethod
    def post(request, pk):
        new_request = request.POST.copy()
        new_request['sender'] = request.user.pk
        new_request['receiver'] = (User.objects.get(pk=pk)).pk

        form = ChatForm(new_request)
        if form.is_valid():
            form.save()
            return redirect(f'/message/{pk}')