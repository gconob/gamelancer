# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamelancer_main', '0002_auto_20170409_0204'),
    ]

    operations = [
        migrations.RenameField(
            model_name='privatenotice',
            old_name='actor',
            new_name='act_user',
        ),
        migrations.RenameField(
            model_name='privatenotice',
            old_name='reader',
            new_name='read_user',
        ),
        migrations.AddField(
            model_name='privatenotice',
            name='type',
            field=models.IntegerField(null=True, choices=[(1, '프로젝트 등록'), (2, '프로젝트 지원'), (3, '프로젝트 계약')]),
        ),
    ]
