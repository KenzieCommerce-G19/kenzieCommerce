# Generated by Django 4.2.2 on 2023-07-03 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_isavailable'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='isAvailable',
            new_name='is_available',
        ),
    ]
