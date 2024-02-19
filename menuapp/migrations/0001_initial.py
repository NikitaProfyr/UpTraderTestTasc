# Generated by Django 4.0.6 on 2024-02-17 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Название элемента меню')),
            ],
            options={
                'verbose_name': 'Элемент меню',
            },
        ),
    ]
