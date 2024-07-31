from django.urls import resolve


def get_named_url(current_url):
    """ Функция для получения текущего именованного url """

    resolved_url = resolve(current_url)

    if resolved_url:
        current_named_url = resolved_url.url_name
        current_namespace = resolved_url.namespace

        if current_namespace:
            named_url = f'{current_namespace}:{current_named_url}'

        else:
            named_url = f'{current_named_url}'

    else:
        named_url = ''

    return named_url


def convert_menu_items_to_menu_tree(menu_items):
    """ Функция преобразует элементы меню в древовидное меню """

    tree = []
    children_dict = {item.id: [] for item in menu_items}

    for item in menu_items:
        if item.parent_id:
            children_dict[item.parent_id].append(item)
        else:
            tree.append((item, []))

    def build_tree(parent_item):
        if parent_item.id in children_dict:
            return parent_item, [build_tree(child) for child in children_dict[parent_item.id]]
        return parent_item, []

    return list(build_tree(item[0]) for item in tree)
