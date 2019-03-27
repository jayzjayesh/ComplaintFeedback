# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-21 05:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_post_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(choices=[('faculty', 'FACULTY'), ('office', 'OFFICE'), ('committe', 'COMMITTE'), ('campus', 'CAMPUS')], default='Faculty', max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='favorite_fruit',
            field=models.CharField(default='FACULTY', max_length=10),
        ),
    ]