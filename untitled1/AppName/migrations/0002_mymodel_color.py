# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-13 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppName', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='color',
            field=models.CharField(default='red', max_length=7),
            preserve_default=False,
        ),
    ]