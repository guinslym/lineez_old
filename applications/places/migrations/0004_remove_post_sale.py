# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-07 03:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_auto_20161105_2050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='sale',
        ),
    ]