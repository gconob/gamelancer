# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gamelancer_main', '0004_auto_20170409_0245'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivateNotice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('desc', models.CharField(max_length=1024)),
                ('type', models.IntegerField(choices=[(1, '프로젝트 등록'), (2, '프로젝트 지원'), (3, '프로젝트 계약')])),
                ('notice_time', models.DateTimeField(auto_now_add=True)),
                ('actor', models.ForeignKey(related_name='actor', to=settings.AUTH_USER_MODEL)),
                ('reader', models.ForeignKey(related_name='reader', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
