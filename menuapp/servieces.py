from django.db.models import QuerySet

from menuapp.models import MenuItem, SubMenuItem


def get_all_menu_item() -> QuerySet:
    """Получить все элементы меню и связанные с ними под-элементы"""
    return MenuItem.objects.prefetch_related('submenuitems')


def get_related_sub_menu_items(id_item: int) -> QuerySet:
    """Получить все элементы под меню, конкретного элемента меню"""
    return SubMenuItem.objects.select_related('menu_item').filter(menu_item=id_item)


def get_current_sub_menu_item(id_item: int) -> QuerySet:
    """Получить данные конкретного под-элемента меню"""
    return SubMenuItem.objects.get(pk=id_item)
