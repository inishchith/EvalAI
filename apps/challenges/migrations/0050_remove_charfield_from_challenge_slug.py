# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-01 06:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("challenges", "0049_add_slug_field_in_challenge_phase")]

    operations = [
        migrations.AlterField(
            model_name="challenge",
            name="slug",
            field=models.SlugField(max_length=200, null=True, unique=True),
        )
    ]
