from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from profile_app.forms.login_form import LoginForm


class Login(LoginView):
    form_class = LoginForm
    template_name = 'profile_app/login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('main_page')
