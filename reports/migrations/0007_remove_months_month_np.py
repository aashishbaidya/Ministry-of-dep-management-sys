# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-14 06:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_auto_20170714_0643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='months',
            name='month_np',
        ),
    ]
