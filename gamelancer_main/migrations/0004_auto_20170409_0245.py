# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamelancer_main', '0003_auto_20170409_0241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='privatenotice',
            name='act_user',
        ),
        migrations.RemoveField(
            model_name='privatenotice',
            name='project',
        ),
        migrations.RemoveField(
            model_name='privatenotice',
            name='read_user',
        ),
        migrations.DeleteModel(
            name='PrivateNotice',
        ),
    ]
