# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-10 18:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mangaki', '0036_merge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anime',
            old_name='author',
            new_name='deprecated_author',
        ),
        migrations.RenameField(
            model_name='anime',
            old_name='composer',
            new_name='deprecated_composer',
        ),
        migrations.RenameField(
            model_name='anime',
            old_name='director',
            new_name='deprecated_director',
        ),
        migrations.RenameField(
            model_name='manga',
            old_name='mangaka',
            new_name='deprecated_mangaka',
        ),
        migrations.RenameField(
            model_name='manga',
            old_name='writer',
            new_name='deprecated_writer',
        ),
    ]
