# Generated by Django 3.2.4 on 2021-06-17 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_cart_sofrt_delete'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='sofrt_delete',
            new_name='soft_delete',
        ),
    ]