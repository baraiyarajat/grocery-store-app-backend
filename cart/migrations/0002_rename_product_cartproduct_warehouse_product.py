# Generated by Django 4.1.3 on 2022-12-02 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartproduct',
            old_name='product',
            new_name='warehouse_product',
        ),
    ]