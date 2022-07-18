from django.contrib.auth.decorators import login_required
from django.urls import path

from .views.editing import EditingProfile
from .views.login import Login
from .views.logout import user_logout
from .views.my_profile import Profile
from .views.profile import ProfileUserView
from .views.registration import Register
from .views.user_search import UserSearchListView

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', user_logout, name='logout'),
    path('myprofile/', login_required(Profile.as_view(), login_url='login'), name='my_profile'),
    path('profile/<int:pk>', login_required(ProfileUserView.as_view()), name='profile'),
    path('editing/', login_required(EditingProfile.as_view()), name='editing'),
    path('search/', UserSearchListView.as_view(), name='user_search'),
    ]