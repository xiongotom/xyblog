# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 11:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('pwd', models.CharField(max_length=32)),
            ],
        ),
    ]
