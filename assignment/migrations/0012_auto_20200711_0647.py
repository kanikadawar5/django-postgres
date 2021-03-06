# Generated by Django 3.0.8 on 2020-07-11 06:47

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0011_auto_20200711_0640'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='values',
            options={'verbose_name': 'Kanika Dawar Assignment'},
        ),
        migrations.AddField(
            model_name='values',
            name='supported_values',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20, null=True), blank=True, max_length=2000, null=True, size=None, verbose_name='supported_values'),
        ),
        migrations.AddField(
            model_name='values',
            name='type',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20, null=True), blank=True, max_length=2000, null=True, size=None, verbose_name='type'),
        ),
        migrations.AddField(
            model_name='values',
            name='values',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20, null=True), blank=True, max_length=2000, null=True, size=None, verbose_name='values'),
        ),
    ]
