# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-23 08:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_grant_approve'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSubscribedGrant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Grant')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]