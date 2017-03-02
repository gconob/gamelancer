# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamelancer_main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('userid', models.CharField(max_length=140)),
                ('password', models.CharField(max_length=255)),
                ('firstname', models.CharField(max_length=140)),
                ('lastname', models.CharField(max_length=140)),
                ('email', models.EmailField(max_length=254)),
                ('usertype', models.PositiveSmallIntegerField()),
                ('emailvalidation', models.BooleanField()),
            ],
        ),
    ]
