# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_auto_20150424_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient_item',
            name='mesured_in',
            field=models.ForeignKey(blank=True, to='recipe.Messurments', null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='mesured_in',
            field=models.ForeignKey(blank=True, to='recipe.Messured_in', null=True),
        ),
    ]
