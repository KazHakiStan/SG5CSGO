from django.shortcuts import render
from django.views import View


class Profile(View):

    @staticmethod
    def get(request):

        context = {
            'title': 'Информация о вашем аккаунте',
        }

        return render(request, 'profile_app/my_profile.html', context)
