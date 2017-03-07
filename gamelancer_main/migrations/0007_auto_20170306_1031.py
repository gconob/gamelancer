# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamelancer_main', '0006_auto_20170306_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address1',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address2',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='cell_phone_number',
            field=models.CharField(default='0', max_length=140),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_complete',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='usertype',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='zipcode',
            field=models.CharField(default='', max_length=10),
        ),
    ]
