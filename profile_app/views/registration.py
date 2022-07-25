import logging

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from profile_app.forms.register_form import RegisterUserForm
from profile_app.tasks import verify_email

logged = logging.getLogger('main_page')


class Register(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "profile_app/register.html"

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('main_page')
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.save()
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'],)
        login(self.request, user)
        return HttpResponseRedirect(reverse('main_page'))


class RegisterEmail(CreateView):

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('main_page')
        return super().dispatch(*args, **kwargs)

    def get(self, request):

        form = RegisterUserForm
        context = {
            'title': 'Регистрация ',
            'form': form
        }
        return render(request, 'profile_app/register.html', context)

    def post(self, request):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Отправка письма для верификации почты (написано в utils.py)

            current_site = get_current_site(request)
            logging.info(verify_email(current_site.domain, user.pk))
            return redirect('confirm_email')

        else:
            messages.error(request, 'Ошибка регистрации. Попробуйте снова')
            context = {
                'title': 'Регистрация ',
                'form': form
            }
            return render(request, 'profile_app/register.html', context)
