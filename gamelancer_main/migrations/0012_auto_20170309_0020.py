# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamelancer_main', '0011_auto_20170308_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='categery4',
            field=models.CharField(max_length='32', choices=[('무관', '무관'), ('RPG', 'RPG'), ('SNG', 'SNG'), ('FPS', 'FPS'), ('AOS', 'AOS'), ('Sports', 'Sports'), ('Gamble', 'Gamble')]),
        ),
        migrations.AlterField(
            model_name='project',
            name='category1',
            field=models.CharField(max_length='32', choices=[('무관', '무관'), ('턴키', '턴키'), ('기획', '기획'), ('서버', '서버 프로그램')]),
        ),
        migrations.AlterField(
            model_name='project',
            name='category2',
            field=models.CharField(max_length='32', choices=[('무관', '무관'), ('C++', 'C++'), ('Unity3D', 'Unity3D'), ('Unreal Engilne', 'Unreal Engine'), ('3D Max', '3D MAX'), ('PhotoShop', 'photoshop')]),
        ),
        migrations.AlterField(
            model_name='project',
            name='category3',
            field=models.CharField(max_length='32', choices=[('무관', '무관'), ('모바일', '모바일'), ('온라인 PC', '온라인 PC'), ('웹게임', '웹게임'), ('콘솔', '콘솔'), ('아케이드', '아케이드')]),
        ),
        migrations.AlterField(
            model_name='project',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
    ]
