# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='note',
            field=models.TextField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='time_cooking',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='time_preperation',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='time_total',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='title_other',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
    ]
