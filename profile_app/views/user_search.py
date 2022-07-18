from django.contrib.auth.models import User
from django.db.models import Q
from django.views.generic import ListView


class UserSearchListView(ListView):

    model = User
    queryset = User.objects.all()
    template_name = "profile_app/user_search.html"
    context_object_name = "search_list"

    def get_queryset(self):
        queryset = super(UserSearchListView, self).get_queryset()
        q = self.request.GET.get("q")

        if q:

            return queryset.filter(Q(username__startswith=q))
        return None
