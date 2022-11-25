# Generated by Django 4.1.3 on 2022-11-25 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('warehouse', '0002_selectedwarehouse'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_type', models.CharField(default='home', max_length=50)),
                ('address_line_1', models.CharField(max_length=300)),
                ('address_line_2', models.CharField(max_length=300)),
                ('pincode', models.CharField(max_length=8)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.warehouse')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
