from django.db import models

# Create your models here.


class MenuItem(models.Model):
    title = models.CharField(null=False, max_length=30, verbose_name='Название элемента меню')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Элемент меню'
        verbose_name_plural = 'Элементы меню'


class SubMenuItem(models.Model):
    title = models.CharField(null=False, max_length=30, verbose_name='Название элемента под-меню')
    description = models.TextField(null=False, max_length=100, verbose_name='Описание элемента под-меню')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, verbose_name='Элемент меню',  related_name='submenuitems')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Элемент под-меню'
        verbose_name_plural = 'Элементы под-меню'

