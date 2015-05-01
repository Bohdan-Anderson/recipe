# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_auto_20150424_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messurments',
            name='types',
            field=models.ForeignKey(to='recipe.Messured_in', blank=True),
        ),
    ]
