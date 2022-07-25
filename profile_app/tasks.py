from celery import shared_task
from django.contrib.auth.models import User
from django.core import mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator as token_generator

from SG5CSGO.settings import EMAIL_HOST_USER


@shared_task
def verify_email(site, user_pk):
    user = User.objects.get(pk=user_pk)

    context = {
        'user': user,
        'domain': site,
        'uid': urlsafe_base64_encode(force_bytes(user_pk)),
        'token': token_generator.make_token(user),
    }

    message = render_to_string(
        template_name='profile_app/email.html',
        context=context,
    )

    with mail.get_connection() as connection:
        email = EmailMessage(
            subject='Verify email check',
            body=message,
            from_email=EMAIL_HOST_USER,
            to=[user.email],
            connection=connection,
        )

        email.send(fail_silently=False)