from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path

from publication_app.api.views.likes import LikesView
from publication_app.api.views.posts import PostsView
from publication_app.views.delete_post import post_delete
from publication_app.views.editing import EditImagePost
from publication_app.views.new_post import AddPost
from publication_app.views.post import PostView
from publication_app.views.posts import Posts

urlpatterns = [
    path('posts/', Posts.as_view(), name='posts'),
    path('post/<int:pk>', login_required(PostView.as_view()), name='post'),
    path('new_post/', login_required(AddPost.as_view()), name='new_post'),
    path('post_red/<int:pk>', login_required(EditImagePost.as_view()), name='post_red'),
    path('post_del/<int:pk>', login_required(post_delete), name='post_del'),
    path('api/posts/', PostsView.as_view({'get': 'list'}), name='api-posts'),
    path('api/likes/', LikesView.as_view({'get': 'list'}), name='api-likes'),
]