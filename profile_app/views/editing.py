from django.shortcuts import render, redirect
from django.views import View

from profile_app.forms.profile_edit_form import UserEditForm, ProfileEditForm


class EditingProfile(View):

    @staticmethod
    def get(request):

        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

        context = {
            'title': 'Редактирование профиля',
            'user_form': user_form,
            'profile_form': profile_form,
        }

        return render(
            request,
            'profile_app/editing.html',
            context
        )

    @staticmethod
    def post(request):

        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('my_profile')