from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View


class ProfileUserView(View):
    @staticmethod
    def get(request, pk):
        users = get_object_or_404(User, pk=pk)

        if users.pk == request.user.pk:
            return redirect('profile')

        context = {
            'title': f'Профиль {users.username}',
            'users': users,
        }
        return render(request, 'profile_app/profile.html', context)