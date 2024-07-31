from django.contrib import admin

from tree.models import MenuItem


@admin.register(MenuItem)
class MenuItemAdminModel(admin.ModelAdmin):
    """ Админка для меню """

    list_display = ('name', 'menu_name', 'parent', 'url', 'named_url')
    list_filter = ('menu_name',)
    search_fields = ('name', 'url', 'named_url')
