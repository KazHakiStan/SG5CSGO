from django.conf.urls import include
from django.contrib import admin
from django.urls import path, re_path

# apipatterns = [
#     re_path(r'^', include('publication_app.api.urls')),
# ]
from likes_app.views import add_like_post
from likes_app.views.add_dislike_comment import AddDislikeComment
from likes_app.views.add_dislike_post import AddDislike
from likes_app.views.add_like_comment import AddLikeComment
from likes_app.views.add_like_post import AddLike

urlpatterns = [
    # re_path(r'^api/v1/', include(apipatterns, namespace='api')),
    # re_path(r'^admin/', admin.site.urls),
    path('<int:pk>/like/', AddLike.as_view(), name='like'),
    path('<int:pk>/dislike/', AddDislike.as_view(), name='dislike'),
    path('<int:pk>/like_c/', AddLikeComment.as_view(), name='like_c'),
    path('<int:pk>/dislike_c', AddDislikeComment.as_view(), name='dislike_c')
]