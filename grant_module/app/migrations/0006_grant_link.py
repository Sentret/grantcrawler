# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-24 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_usersubscribedgrant'),
    ]

    operations = [
        migrations.AddField(
            model_name='grant',
            name='link',
            field=models.CharField(default='', max_length=300),
        ),
    ]