# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-18 20:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20171019_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete='id', to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
    ]
