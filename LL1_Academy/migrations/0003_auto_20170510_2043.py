# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-10 20:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LL1_Academy', '0002_auto_20170510_1903'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='parsetable',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='parsetable',
            name='gid',
        ),
        migrations.AddField(
            model_name='grammar',
            name='nonTerminals',
            field=models.CharField(default='A', max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grammar',
            name='startSymbol',
            field=models.CharField(default='A', max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='ParseTable',
        ),
    ]
