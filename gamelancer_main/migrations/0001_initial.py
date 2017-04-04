# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('score', models.FloatField()),
                ('desc', models.TextField()),
                ('evaluated', models.ForeignKey(related_name='evaluated', to=settings.AUTH_USER_MODEL)),
                ('evaluator', models.ForeignKey(related_name='evaluator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PartnerEducation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('school', models.CharField(max_length=140)),
                ('major', models.CharField(max_length=64)),
                ('degree', models.CharField(max_length=32, choices=[('박사', '박사'), ('석사', '석사'), ('학사', '학사'), ('없음', '없음')])),
                ('type', models.CharField(max_length=140, choices=[('대학원', '대학원'), ('대학교', '대학교'), ('전문대', '전문대'), ('고등학교', '고등학교')])),
                ('status', models.CharField(max_length=140, choices=[('졸업', '졸업'), ('졸업예정', '졸업예정'), ('재학중', '재학중'), ('중퇴', '중퇴')])),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PartnerLicense',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=64)),
                ('level', models.CharField(max_length=64, null=True)),
                ('institution', models.CharField(max_length=64, null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PartnerTechnic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('type', models.CharField(max_length=140)),
                ('level', models.CharField(max_length=32, choices=[('특급', '특급'), ('고급', '고급'), ('중급', '중급'), ('하급', '하급')])),
                ('time', models.CharField(max_length=64, choices=[('10년 이상', '10년 이상'), ('5년이상 10년미만', '5년이상 10년미만'), ('3년이상 5년미만', '3년이상 5년 미만'), ('1년이상 3년미만', '1년이상 3년미만'), ('1년이하', '1년이하')])),
                ('main', models.BooleanField(default=False)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PartnerWorkHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('company', models.CharField(max_length=140)),
                ('department', models.CharField(max_length=140)),
                ('title', models.CharField(max_length=140)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=32)),
                ('category1', models.CharField(max_length='32', default='무관', choices=[('무관', '무관'), ('턴키', '턴키'), ('기획', '기획'), ('서버', '서버 프로그램')])),
                ('category2', models.CharField(max_length='32', default='무관', choices=[('무관', '무관'), ('모바일', '모바일'), ('온라인 PC', '온라인 PC'), ('웹게임', '웹게임'), ('콘솔', '콘솔'), ('아케이드', '아케이드')])),
                ('category3', models.CharField(max_length='32', default='무관', choices=[('무관', '무관'), ('RPG', 'RPG'), ('SNG', 'SNG'), ('FPS', 'FPS'), ('AOS', 'AOS'), ('Sports', 'Sports'), ('Gamble', 'Gamble')])),
                ('desc', models.TextField(null=True)),
                ('start_day', models.DateField(null=True)),
                ('end_day', models.DateField(null=True)),
                ('participation_ratio', models.IntegerField()),
                ('technical_tag', models.CharField(max_length=128, null=True)),
                ('image1', models.ImageField(null=True, upload_to='portfolio')),
                ('image2', models.ImageField(null=True, upload_to='portfolio')),
                ('image3', models.ImageField(null=True, upload_to='portfolio')),
                ('image4', models.ImageField(null=True, upload_to='portfolio')),
                ('image5', models.ImageField(null=True, upload_to='portfolio')),
                ('image1desc', models.CharField(max_length=140, null=True)),
                ('image2desc', models.CharField(max_length=140, null=True)),
                ('image3desc', models.CharField(max_length=140, null=True)),
                ('image4desc', models.CharField(max_length=140, null=True)),
                ('image5desc', models.CharField(max_length=140, null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PrivateNotice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=64)),
                ('desc', models.TextField()),
                ('notice_time', models.DateTimeField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('usertype', models.SmallIntegerField(default=0)),
                ('desc', models.TextField(null=True)),
                ('companytype', models.CharField(max_length=64, null=True)),
                ('establish_date', models.DateField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('identity_verified', models.BooleanField(default=False)),
                ('email_verified', models.BooleanField(default=False)),
                ('contact_verified', models.BooleanField(default=False)),
                ('profile_complete', models.BooleanField(default=False)),
                ('cell_phone_number', models.CharField(max_length=140, null=True)),
                ('phone_number', models.CharField(max_length=140, null=True)),
                ('fax_number', models.CharField(max_length=140, null=True)),
                ('address1', models.CharField(max_length=255, null=True)),
                ('address2', models.CharField(max_length=255, null=True)),
                ('zipcode', models.CharField(max_length=10, null=True)),
                ('image', models.ImageField(null=True, upload_to='user')),
                ('account_bank', models.CharField(max_length=64, null=True)),
                ('account_owner_name', models.CharField(max_length=64, null=True)),
                ('account_number', models.CharField(max_length=64, null=True)),
                ('company_name', models.CharField(max_length=64, null=True)),
                ('business_registration_number', models.CharField(max_length=64, null=True)),
                ('company_representative', models.CharField(max_length=64, null=True)),
                ('business_address', models.CharField(max_length=128, null=True)),
                ('tax_email', models.EmailField(max_length=254, null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=140)),
                ('desc', models.TextField()),
                ('category1', models.CharField(max_length='32', default='무관', choices=[('무관', '무관'), ('턴키', '턴키'), ('기획', '기획'), ('서버', '서버 프로그램')])),
                ('category2', models.CharField(max_length='32', default='무관', choices=[('무관', '무관'), ('모바일', '모바일'), ('온라인 PC', '온라인 PC'), ('웹게임', '웹게임'), ('콘솔', '콘솔'), ('아케이드', '아케이드')])),
                ('categery3', models.CharField(max_length='32', default='무관', choices=[('무관', '무관'), ('RPG', 'RPG'), ('SNG', 'SNG'), ('FPS', 'FPS'), ('AOS', 'AOS'), ('Sports', 'Sports'), ('Gamble', 'Gamble')])),
                ('region', models.CharField(max_length=140, null=True)),
                ('technical_tag', models.CharField(max_length=128, null=True)),
                ('duration', models.IntegerField(default=0)),
                ('register_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('work_start_date', models.DateField(null=True)),
                ('closing_date', models.DateField(null=True)),
                ('budget', models.IntegerField(default=0)),
                ('display', models.BooleanField(default=False)),
                ('client', models.ForeignKey(related_name='client', to=settings.AUTH_USER_MODEL)),
                ('partner', models.ForeignKey(null=True, related_name='partner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectApply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('budget', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('comment', models.TextField()),
                ('portfolio_desc', models.TextField()),
                ('portfolio1', models.ForeignKey(null=True, related_name='portfolio1', to='gamelancer_main.Portfolio')),
                ('portfolio2', models.ForeignKey(null=True, related_name='portfolio2', to='gamelancer_main.Portfolio')),
                ('portfolio3', models.ForeignKey(null=True, related_name='portfolio3', to='gamelancer_main.Portfolio')),
                ('project', models.ForeignKey(to='gamelancer_main.Project')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('parent_id', models.IntegerField(default=0)),
                ('secret', models.BooleanField(default=False)),
                ('desc', models.TextField()),
                ('project', models.ForeignKey(to='gamelancer_main.Project')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectConcern',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('project', models.ForeignKey(to='gamelancer_main.Project')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PublicNotice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=64)),
                ('desc', models.TextField()),
                ('notice_date', models.DateField()),
                ('display', models.BooleanField()),
            ],
        ),
    ]
