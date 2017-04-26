# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamelancer_main', '0007_privatenotice_readyn'),
    ]

    operations = [
        migrations.AddField(
            model_name='privatenotice',
            name='project',
            field=models.ForeignKey(null=True, to='gamelancer_main.Project'),
        ),
    ]
