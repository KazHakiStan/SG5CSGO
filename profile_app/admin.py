from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UserAdminBase
from django.utils.html import mark_safe
from django.contrib.auth.admin import User
from profile_app.models import Profile

admin.site.unregister(User)


class ProfileInline(admin.StackedInline):
    model = Profile
    list_display = ('user', 'edited_photo')
    ordering = ('-user',)
    readonly_fields = ('edited_photo',)

    def edited_photo(self, obj):
        if obj.photo:
            return mark_safe(
                f'<a href="{obj.photo.url}">'
                f'<img src="{obj.photo.url}" width="150px" height="150px"/><a href="{obj.photo.url}"/>'
                f'</a>'
            )


@admin.register(User)
class UserAdmin(UserAdminBase):
    inlines = (
        ProfileInline,
    )