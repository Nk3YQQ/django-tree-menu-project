from django import template
from django.db.models import Q

from tree.models import MenuItem
from tree.services import get_named_url, convert_menu_items_to_menu_tree

register = template.Library()


@register.inclusion_tag('tree/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    """ Тэг для создания дерева меню """

    request = context['request']
    current_url = request.path

    menu_items = MenuItem.objects.filter(menu_name=menu_name).select_related('parent')

    menu_tree = convert_menu_items_to_menu_tree(menu_items)

    context['menu_tree'] = menu_tree
    context['current_url'] = current_url

    return context


@register.simple_tag(takes_context=True)
def get_current_title(context):
    request = context['request']
    current_url = request.path

    named_url = get_named_url(current_url)

    menu_item = MenuItem.objects.filter(
        Q(url=current_url) | Q(named_url=named_url)
    ).select_related('parent').first()

    if not menu_item:
        return ''

    return menu_item.name
