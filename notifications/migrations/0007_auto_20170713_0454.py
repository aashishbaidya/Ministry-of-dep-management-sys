# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-13 04:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0006_notification_group'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='group',
            new_name='detail_url',
        ),
    ]