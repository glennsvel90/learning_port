# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 21:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_auto_20170531_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='multiplechoicequestion',
            name='correct',
        ),
        migrations.RemoveField(
            model_name='truefalsequestion',
            name='correct',
        ),
    ]