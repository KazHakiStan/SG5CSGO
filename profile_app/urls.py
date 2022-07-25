from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import TemplateView

from .views.editing import EditingProfile
from .views.email import EmailVerify
from .views.login import Login
from .views.logout import user_logout
from .views.my_profile import Profile
from .views.profile import ProfileUserView
from .views.registration import Register, RegisterEmail
from .views.user_search import UserSearchListView

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('register/', RegisterEmail.as_view(), name='register'),
    path('logout/', user_logout, name='logout'),
    path('myprofile/', login_required(Profile.as_view(), login_url='login'), name='my_profile'),
    path('profile/<int:pk>', login_required(ProfileUserView.as_view()), name='profile'),
    path('editing/', login_required(EditingProfile.as_view()), name='editing'),
    path('search/', UserSearchListView.as_view(), name='user_search'),
    path('verify_email/<uidb64>/<token>/', EmailVerify.as_view(), name='email',),
    path('confirm_email/', TemplateView.as_view(template_name='profile_app/confirm_email.html'), name='confirm_email'),
    path('invalid_email/', TemplateView.as_view(template_name='profile_app/invalid_email.html'), name='invalid_email'),
    ]