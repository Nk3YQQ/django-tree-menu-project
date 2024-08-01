import json

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


def open_json_file_and_read_data(filepath):
    """ Функция открывает json файл и считывает данные """

    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)


def create_menu_for_command(menu_item_model, load_data):
    """ Функция создаёт объекты меню на основе полученных данных """

    def create_menu_item(item_data, parent=None):
        item = menu_item_model.objects.create(
            name=item_data['name'],
            menu_name=item_data['menu_name'],
            url=item_data.get('url'),
            named_url=item_data.get('named_url'),
            parent=parent
        )

        for child_data in item_data.get('children', []):
            create_menu_item(child_data, parent=item)

    for data in load_data:
        create_menu_item(data)
