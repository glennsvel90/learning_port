# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-05 06:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_remove_multiplechoicequestion_correct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='truefalsequestion',
            name='correct',
        ),
    ]
