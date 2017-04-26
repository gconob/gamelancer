# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('gamelancer_main', '0005_privatenotice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privatenotice',
            name='actor',
            field=models.ForeignKey(null=True, related_name='actor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='privatenotice',
            name='desc',
            field=models.CharField(max_length=1024, null=True),
        ),
    ]
