# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-06 15:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RestAPI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('district', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('postcode', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'address',
            },
        ),
        migrations.CreateModel(
            name='communication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=100)),
                ('preferred', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'communication',
            },
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system', models.CharField(max_length=100)),
                ('use', models.CharField(max_length=100, null=True)),
                ('value', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'contact',
            },
        ),
        migrations.CreateModel(
            name='name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefix', models.CharField(blank=True, max_length=100, null=True)),
                ('given_name', models.CharField(db_index=True, max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('family_name', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('suffix', models.CharField(blank=True, max_length=100, null=True)),
                ('language', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'name',
            },
        ),
        migrations.CreateModel(
            name='organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_name', models.CharField(max_length=20)),
                ('code_number', models.CharField(blank=True, max_length=20, null=True)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'organization',
            },
        ),
        migrations.RemoveField(
            model_name='identifier',
            name='period',
        ),
        migrations.RemoveField(
            model_name='identifier',
            name='system',
        ),
        migrations.RemoveField(
            model_name='identifier',
            name='use',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='active',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='name',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='telecom',
        ),
        migrations.AddField(
            model_name='identifier',
            name='end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='identifier',
            name='facility',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='identifier',
            name='start',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='birth_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='deceased',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='deceased_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='marital_status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='nationality',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='religion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='row_id',
            field=models.CharField(default=None, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='identifier',
            name='type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='identifier',
            name='value',
            field=models.CharField(blank=True, db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization', to='RestAPI.Patient'),
        ),
        migrations.AddField(
            model_name='name',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name', to='RestAPI.Patient'),
        ),
        migrations.AddField(
            model_name='contact',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact', to='RestAPI.Patient'),
        ),
        migrations.AddField(
            model_name='communication',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='communication', to='RestAPI.Patient'),
        ),
        migrations.AddField(
            model_name='address',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='RestAPI.Patient'),
        ),
    ]
