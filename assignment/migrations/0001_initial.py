# Generated by Django 3.0.8 on 2020-07-09 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Values',
            fields=[
                ('value_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Value ID')),
                ('invalid_trigger', models.CharField(max_length=100, verbose_name='invalid_trigger')),
                ('key', models.CharField(max_length=100, verbose_name='key')),
                ('name', models.CharField(blank=True, max_length=150, verbose_name='Name')),
                ('reuse', models.CharField(blank=True, max_length=150, verbose_name='Middle Name')),
                ('support_multiple', models.CharField(blank=True, max_length=150, verbose_name='Middle Name')),
                ('pick_first', models.CharField(blank=True, max_length=150, verbose_name='Middle Name')),
                ('supported_values', models.CharField(blank=True, max_length=150, verbose_name='Middle Name')),
                ('type', models.CharField(blank=True, max_length=150, verbose_name='Middle Name')),
                ('validation_parser', models.CharField(blank=True, max_length=150, verbose_name='Middle Name')),
                ('values', models.CharField(blank=True, max_length=150, verbose_name='Middle Name')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Kanika Dawar Assignment',
                'db_table': 'values_requests',
                'ordering': ('value_id',),
            },
        ),
    ]
