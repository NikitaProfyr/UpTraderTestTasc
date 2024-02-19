from django.urls import path

from menuapp.views import MainMenuView, MenuItemDetailView, SubMenuItemDetailView

urlpatterns = [
    path('main/', MainMenuView.as_view(), name='MainMenuView'),
    path('<int:id_item>/', MenuItemDetailView.as_view(), name='MenuItemDetailView'),
    path('sub-menu/<int:id_item>/', SubMenuItemDetailView.as_view(), name='SubMenuItemDetailView')
]