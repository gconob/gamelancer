# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamelancer_main', '0012_auto_20170309_0020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='technical_tag',
        ),
        migrations.AddField(
            model_name='project',
            name='technical_tag1',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='technical_tag2',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='technical_tag3',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='technical_tag4',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='technical_tag5',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
