# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-21 06:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20171021_1118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='portfolio_site',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='Name',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='Roll_Number',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
