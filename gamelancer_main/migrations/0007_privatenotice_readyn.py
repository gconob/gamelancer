# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamelancer_main', '0006_auto_20170409_0300'),
    ]

    operations = [
        migrations.AddField(
            model_name='privatenotice',
            name='readyn',
            field=models.BooleanField(default=False),
        ),
    ]
