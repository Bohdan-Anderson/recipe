# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ethnicity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500)),
                ('created', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500)),
                ('created', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500)),
                ('name_other', models.CharField(max_length=500, null=True, blank=True)),
                ('notes', models.TextField(max_length=1000, blank=True)),
                ('slug', models.SlugField(blank=True)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient_Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ammount_number', models.FloatField(null=True, blank=True)),
                ('ammount_string', models.TextField(max_length=1000, blank=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('Ingredient', models.ForeignKey(to='recipe.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Messured_in',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Messurments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500)),
                ('notes', models.TextField(max_length=1000, blank=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('types', models.ForeignKey(to='recipe.Messured_in')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500)),
                ('title_other', models.CharField(max_length=500)),
                ('time_preperation', models.FloatField(blank=True)),
                ('time_cooking', models.FloatField(blank=True)),
                ('time_total', models.FloatField(blank=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True)),
                ('ethnicity', models.ManyToManyField(to='recipe.Ethnicity', blank=True)),
                ('foodType', models.ManyToManyField(to='recipe.FoodType', blank=True)),
                ('ingredients', models.ManyToManyField(to='recipe.Ingredient_Item')),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.IntegerField(default=99, null=True, blank=True)),
                ('note', models.TextField(max_length=1000, blank=True)),
                ('highLight', models.TextField(max_length=1000, blank=True)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='steps',
            field=models.ManyToManyField(to='recipe.Step'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='mesured_in',
            field=models.ForeignKey(blank=True, to='recipe.Messurments', null=True),
        ),
    ]
