# Generated by Django 5.1 on 2024-08-19 07:01

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('relation_to', models.IntegerField(choices=[(0, 'outerwear'), (1, 'underwear'), (2, 'accessories')])),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='%Y%m%d')),
            ],
        ),
        migrations.CreateModel(
            name='Sizes',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('sale_status', models.IntegerField(choices=[(1, 'Sale'), (0, 'Not sale')], default=0)),
                ('price', models.FloatField()),
                ('stock_status', models.IntegerField(choices=[(1, 'In stock'), (0, 'Out stock')], default=0)),
                ('sex', models.IntegerField(choices=[(3, 'Men'), (2, 'Woman'), (1, 'Boy'), (0, 'Girl')])),
                ('seazon', models.IntegerField(choices=[(4, 'Multiseazon'), (3, 'Winter'), (2, 'Spring'), (1, 'Summer'), (0, 'autumn')])),
                ('reviews', models.JSONField()),
                ('categories_fk', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='categories', to='api.categories')),
                ('images_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='api.images')),
                ('sizes_fk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sizes', to='api.sizes')),
            ],
        ),
    ]
