# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gamelancer_main', '0007_auto_20170306_1031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField(default=1)),
                ('title', models.CharField(max_length=140)),
                ('desc', models.TextField()),
                ('rootcategory', models.SmallIntegerField(default=0)),
                ('childcategory', models.SmallIntegerField(default=1)),
                ('region_code1', models.IntegerField(default=0)),
                ('region_code2', models.IntegerField(default=0)),
                ('technical_tag', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_id', models.IntegerField()),
                ('category_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProjectCategory_Master',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=140)),
                ('parent_id', models.IntegerField(default=0)),
                ('duration', models.IntegerField(default=0)),
                ('register_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('work_start_date', models.DateField(null=True)),
                ('closing_date', models.DateField(null=True)),
                ('budget', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='companytype',
            field=models.SmallIntegerField(default=0),
        ),
    ]
