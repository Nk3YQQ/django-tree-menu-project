from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdminModel(admin.ModelAdmin):
    """ Админка для пользователей """

    list_display = ('first_name', 'last_name', 'email')
    list_filter = ('last_name',)
