# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gamelancer_main', '0008_auto_20170307_0931'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectcategory_master',
            name='budget',
        ),
        migrations.RemoveField(
            model_name='projectcategory_master',
            name='closing_date',
        ),
        migrations.RemoveField(
            model_name='projectcategory_master',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='projectcategory_master',
            name='register_time',
        ),
        migrations.RemoveField(
            model_name='projectcategory_master',
            name='work_start_date',
        ),
        migrations.AddField(
            model_name='project',
            name='budget',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='closing_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='duration',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='register_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='project',
            name='work_start_date',
            field=models.DateField(null=True),
        ),
    ]
