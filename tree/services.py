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

    items_dict = {item.id: item for item in menu_items}
    tree = {}

    for item in menu_items:
        print(item.parent_id)

        if not item.parent_id:
            tree[item.id] = (item, [])

        else:
            parent = items_dict.get(item.parent_id)
            print(parent)
            if parent:
                if parent.id not in tree:
                    tree[parent.id] = (parent, [])
                tree[parent.id][1].append((item, []))

    return list(tree.values())
