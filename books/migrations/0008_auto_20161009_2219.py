# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-09 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20161009_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_commented',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]