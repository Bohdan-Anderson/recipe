# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_auto_20150425_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messurments',
            name='types',
            field=models.ForeignKey(blank=True, to='recipe.Messured_in', null=True),
        ),
    ]
