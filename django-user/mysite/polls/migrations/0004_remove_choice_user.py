# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 10:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_choice_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='user',
        ),
    ]
