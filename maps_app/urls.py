from django.urls import path

from maps_app.views import MainPage

urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('maps/', MainPage.as_view(), name='maps')
]