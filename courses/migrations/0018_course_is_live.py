# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-11 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0017_quiz_times_taken'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_live',
            field=models.BooleanField(default=False),
        ),
    ]
