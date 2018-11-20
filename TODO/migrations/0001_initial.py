# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-16 07:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('level', models.CharField(max_length=10)),
                ('add_time', models.CharField(max_length=150)),
                ('complete_time', models.CharField(max_length=150)),
                ('is_complete', models.CharField(max_length=10)),
                ('is_send_mail', models.IntegerField()),
                ('time_day', models.CharField(max_length=24)),
                ('time_hours', models.CharField(max_length=60)),
                ('time_minute', models.CharField(max_length=60)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_list', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-add_time'],
            },
        ),
    ]
