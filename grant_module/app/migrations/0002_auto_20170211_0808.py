# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 08:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grant',
            old_name='name',
            new_name='title',
        ),
    ]
