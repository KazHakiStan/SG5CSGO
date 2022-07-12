from django.shortcuts import render

# Create your views here.
from django.views import View

from maps_app.models import Map


class MainPage(View):
    @staticmethod
    def get(request):
        maps = Map.objects.all()

        context = {
            'title': 'Main page',
            'maps': maps
        }

        return render(request, 'maps_app/main_page.html', context)