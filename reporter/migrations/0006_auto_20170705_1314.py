# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 13:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0005_auto_20170705_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testsuite',
            name='date_run',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]