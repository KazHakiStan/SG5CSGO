from django.contrib import admin
from .models import Friendship


@admin.register(Friendship)
class FriendshipAdmin(admin.ModelAdmin):
    list_filter = ['sender', 'receiver', 'friend']
    list_display = ['sender', 'receiver', 'friend']
    search_fields = ['sender', 'receiver', 'friend']

    class Meta:
        model = Friendship
