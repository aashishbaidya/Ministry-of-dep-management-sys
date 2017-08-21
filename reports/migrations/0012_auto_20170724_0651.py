# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 06:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0011_auto_20170723_0955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lakxya',
            name='fiscal_year',
        ),
        migrations.RemoveField(
            model_name='pragati',
            name='fiscal_year',
        ),
        migrations.AddField(
            model_name='karyakram',
            name='fiscal_year',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pragatiyear', to='reports.FiscalYear', verbose_name='\u0935\u093f\u0924\u094d\u0924\u0940\u092f \u0935\u0930\u094d\u0937'),
            preserve_default=False,
        ),
    ]
