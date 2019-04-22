# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-04-01 08:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_remove_tag_products'),
        ('products', '0011_product_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tags.Tag'),
        ),
    ]