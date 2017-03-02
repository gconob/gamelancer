# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gamelancer_main', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='createtime',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 2, 0, 54, 1, 16798, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='inuse',
            field=models.BooleanField(default=datetime.datetime(2017, 3, 2, 0, 54, 8, 14030, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='logintime',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 2, 0, 54, 20, 862105, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
