# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-12-14 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='konkursimage',
            name='image',
            field=models.ImageField(blank=True, default=None, upload_to='./static/img/'),
        ),
    ]
