# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-25 16:26
from __future__ import unicode_literals

from django.db import migrations, models
import salesforce.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', salesforce.fields.SalesforceAutoField(auto_created=True, db_column='Id', primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('Email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
            options={
                'abstract': False,
                'managed': False,
            },
        ),
    ]
