from django.http import HttpRequest
from django.views import View
from django.views.generic import ListView
from django.shortcuts import render
from menuapp.models import MenuItem
from menuapp.servieces import get_related_sub_menu_items, get_current_sub_menu_item


# Create your views here.


class MainMenuView(ListView):
    model = MenuItem
    template_name = 'main-menu.html'
    context_object_name = 'menu_items'


class MenuItemDetailView(View):
    template_name = 'menu-item-detail.html'

    def get(self, request: HttpRequest, id_item: int):
        sub_menu_items = get_related_sub_menu_items(id_item=id_item)
        context = {
            'menu_items': sub_menu_items
        }
        return render(request, self.template_name, context=context)


class SubMenuItemDetailView(View):
    template_name = 'sub-menu-item-detail.html'

    def get(self, request: HttpRequest, id_item: int):
        sub_menu_items = get_current_sub_menu_item(id_item=id_item)
        context = {
            'menu_item': sub_menu_items
        }
        return render(request, self.template_name, context=context)
