# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-29 10:51
from __future__ import unicode_literals

import bookstudio.books.models
from django.db import migrations, models
import storages.backends.s3boto


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='file_name',
            field=models.FileField(blank=True, null=True, storage=storages.backends.s3boto.S3BotoStorage(acl='bucket-owner-read', bucket='bookstudio-images'), upload_to=bookstudio.books.models.books_directory_path),
        ),
    ]