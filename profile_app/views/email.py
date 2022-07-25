from django.contrib.auth import get_user_model, login
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.utils.http import urlsafe_base64_decode
from django.views import View
from django.contrib.auth.tokens import default_token_generator as token_generator

User = get_user_model()


class EmailVerify(View):

    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)

        if user is not None and token_generator.check_token(user, token):

            user.profile.email_verify = True

            user.profile.save()

            login(request, user)
            return redirect('my_profile')

        return redirect('invalid_email')

    @staticmethod
    def get_user(uidb64):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()

            user = User.objects.get(pk=uid)

        except (TypeError, ValueError, OverflowError,
                User.DoesNotExist, ValidationError):
            user = None
        return user
