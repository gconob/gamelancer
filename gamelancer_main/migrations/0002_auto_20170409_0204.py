# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gamelancer_main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='privatenotice',
            name='title',
        ),
        migrations.RemoveField(
            model_name='privatenotice',
            name='user',
        ),
        migrations.AddField(
            model_name='privatenotice',
            name='actor',
            field=models.ForeignKey(null=True, related_name='actor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='privatenotice',
            name='project',
            field=models.ForeignKey(null=True, to='gamelancer_main.Project'),
        ),
        migrations.AddField(
            model_name='privatenotice',
            name='reader',
            field=models.ForeignKey(default=datetime.datetime(2017, 4, 8, 17, 4, 32, 276688, tzinfo=utc), related_name='reader', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='privatenotice',
            name='desc',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='privatenotice',
            name='notice_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
