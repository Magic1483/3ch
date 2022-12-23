# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=250)),
                ('content', models.CharField(max_length=500)),
                ('img', models.ImageField(blank=True, upload_to='media')),
                ('collection', models.CharField(max_length=100, default='non')),
                ('author', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.TextField()),
                ('image', models.ImageField(null=True, default='static/imgs/no_track_img.png', upload_to='')),
                ('audio_file', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('login', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('nick', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
