# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamelancer_main', '0008_privatenotice_project'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='categery3',
            new_name='category3',
        ),
    ]
