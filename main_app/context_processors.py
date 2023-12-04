from .models import MainMenuItems


def main_menu_items(request):
    items = MainMenuItems.objects.filter(is_visible=True)
    return {'main_menu': items}