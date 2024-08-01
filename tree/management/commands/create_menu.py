from django.core.management import BaseCommand

from config.settings import MAIN_MENU_PATH, PROFILE_MENU_PATH, UNDER_MENU_PATH
from tree.models import MenuItem
from tree.services import open_json_file_and_read_data, create_menu_for_command


class Command(BaseCommand):
    """ Команда создаёт элементы древовидного меню """

    def handle(self, *args, **options):
        main_menu_items = open_json_file_and_read_data(MAIN_MENU_PATH)
        profile_menu_items = open_json_file_and_read_data(PROFILE_MENU_PATH)
        under_menu_items = open_json_file_and_read_data(UNDER_MENU_PATH)

        create_menu_for_command(MenuItem, main_menu_items)
        create_menu_for_command(MenuItem, profile_menu_items)
        create_menu_for_command(MenuItem, under_menu_items)

        self.stdout.write(self.style.SUCCESS('Menu was created'))
