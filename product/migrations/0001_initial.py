# Generated by Django 4.1.3 on 2022-12-15 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=400, null=True)),
                ('description', models.CharField(blank=True, max_length=2000, null=True)),
                ('benefits', models.CharField(blank=True, max_length=2000, null=True)),
                ('how_to_use', models.CharField(blank=True, max_length=2000, null=True)),
                ('disclaimer', models.CharField(blank=True, max_length=2000, null=True)),
                ('image', models.ImageField(max_length=255, null=True, upload_to='photos/product_primary_image')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
    ]
