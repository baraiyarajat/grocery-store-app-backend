# Generated by Django 4.1.3 on 2022-12-24 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('warehouse', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WarehouseProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('discount_rate', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('is_featured', models.BooleanField(default=False)),
                ('feature_reason', models.CharField(blank=True, default='', max_length=512)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.warehouse')),
            ],
            options={
                'unique_together': {('warehouse', 'product')},
            },
        ),
    ]
