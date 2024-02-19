from django.contrib import admin

from menuapp.models import MenuItem, SubMenuItem


# Register your models here.

@admin.register(MenuItem)
class MenuItemModelAdmin(admin.ModelAdmin):
    model = MenuItem


@admin.register(SubMenuItem)
class SubMenuItemModelAdmin(admin.ModelAdmin):
    model = SubMenuItem
