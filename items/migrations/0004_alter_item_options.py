# Generated by Django 4.1.4 on 2022-12-21 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_alter_order_order_duration'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name_plural': 'categories'},
        ),
    ]
