# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamelancer_main', '0009_auto_20170307_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('project_id', models.IntegerField(default=0)),
                ('category', models.CharField(default='0', max_length=140)),
                ('desc', models.TextField(default='0')),
                ('start_day', models.DateField()),
                ('end_day', models.DateField()),
                ('participation_ratio', models.IntegerField()),
                ('technical_tag', models.CharField(max_length=255)),
                ('image1', models.ImageField(upload_to='portfolio')),
                ('image2', models.ImageField(upload_to='portfolio')),
                ('image3', models.ImageField(upload_to='portfolio')),
                ('image4', models.ImageField(upload_to='portfolio')),
                ('image5', models.ImageField(upload_to='portfolio')),
                ('image1desc', models.CharField(max_length=140)),
                ('image2desc', models.CharField(max_length=140)),
                ('image3desc', models.CharField(max_length=140)),
                ('image4desc', models.CharField(max_length=140)),
                ('image5desc', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectApply',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('project_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('budget', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('comment', models.TextField()),
                ('portfolio', models.CharField(max_length=55)),
                ('portfolio_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProjectConcern',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('project_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='childcategory',
        ),
        migrations.RemoveField(
            model_name='project',
            name='region_code1',
        ),
        migrations.RemoveField(
            model_name='project',
            name='region_code2',
        ),
        migrations.RemoveField(
            model_name='project',
            name='rootcategory',
        ),
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.CharField(default='0', max_length=140),
        ),
        migrations.AddField(
            model_name='project',
            name='display',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='region',
            field=models.CharField(null=True, max_length=140),
        ),
        migrations.AlterField(
            model_name='project',
            name='technical_tag',
            field=models.CharField(null=True, max_length=255),
        ),
    ]
