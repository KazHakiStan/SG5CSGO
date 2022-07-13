from django.conf.urls import include
from django.contrib import admin
from django.urls import path, re_path

# apipatterns = [
#     re_path(r'^', include('publication_app.api.urls')),
# ]
from likes_app.views import add_like

urlpatterns = [
    # re_path(r'^api/v1/', include(apipatterns, namespace='api')),
    # re_path(r'^admin/', admin.site.urls),
    path('like/<int:pk>', add_like, name='like_post')
]