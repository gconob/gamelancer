# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamelancer_main', '0010_auto_20170308_0944'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProjectCategory',
        ),
        migrations.DeleteModel(
            name='ProjectCategory_Master',
        ),
        migrations.RemoveField(
            model_name='project',
            name='category',
        ),
        migrations.AddField(
            model_name='project',
            name='categery4',
            field=models.SmallIntegerField(default=0, choices=[(0, '무관'), (1, 'RPG'), (2, 'SNG'), (3, 'FPS'), (4, 'AOS'), (5, 'Sports'), (6, 'Gamble')]),
        ),
        migrations.AddField(
            model_name='project',
            name='category1',
            field=models.SmallIntegerField(default=0, choices=[(0, '무관'), (1, '턴키'), (2, '기획'), (3, '서버 프로그램'), (4, '클라이언트 프로그램'), (5, '웹 프로그램'), (6, '원화'), (7, 'UI'), (8, '2D 그래픽'), (9, '3D 그래픽')]),
        ),
        migrations.AddField(
            model_name='project',
            name='category2',
            field=models.SmallIntegerField(default=0, choices=[(0, '무관'), (1, 'C++'), (2, 'Unity3D'), (3, 'Unreal Engine'), (4, '3D MAX'), (5, 'photoshop')]),
        ),
        migrations.AddField(
            model_name='project',
            name='category3',
            field=models.SmallIntegerField(default=0, choices=[(0, '무관'), (1, '모바일'), (2, '온라인 PC'), (3, '웹게임'), (4, '콘솔'), (5, '아케이드')]),
        ),
    ]
