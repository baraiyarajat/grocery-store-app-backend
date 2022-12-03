# Generated by Django 4.1.3 on 2022-12-02 21:34

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse_product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0004_cartproduct_warehouse'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cartproduct',
            unique_together={('user', 'warehouse_product')},
        ),
    ]
