# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-09 21:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0010_auto_20171109_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcase',
            name='failing_context',
            field=models.CharField(default='', max_length=500),
        ),
    ]
