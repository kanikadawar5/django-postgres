# Generated by Django 3.0.8 on 2020-07-11 07:53

import assignment.models
import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0015_auto_20200711_0715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='values',
            name='values',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.jsonb.JSONField(default=assignment.models.my_default), blank=True, null=True, size=None, verbose_name='values'),
        ),
    ]
