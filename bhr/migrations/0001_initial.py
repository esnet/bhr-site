# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-11-21 21:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import netfields.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cidr', netfields.fields.CidrAddressField(db_index=True, max_length=43)),
                ('source', models.CharField(db_index=True, max_length=30)),
                ('why', models.TextField()),
                ('added', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='date added')),
                ('unblock_at', models.DateTimeField(db_index=True, null=True, verbose_name='date to be unblocked')),
                ('flag', models.CharField(choices=[('N', 'None'), ('I', 'Inbound'), ('O', 'Outbound'), ('B', 'Both')], default='N', max_length=1)),
                ('skip_whitelist', models.BooleanField(default=False)),
                ('forced_unblock', models.BooleanField(default=False)),
                ('unblock_why', models.TextField(blank=True)),
                ('unblock_who', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('who', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BlockEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ident', models.CharField(db_index=True, max_length=50, verbose_name='blocker ident')),
                ('added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('removed', models.DateTimeField(null=True, verbose_name='date removed')),
                ('unblock_at', models.DateTimeField(db_index=True, null=True, verbose_name='date to be unblocked')),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bhr.Block')),
            ],
        ),
        migrations.CreateModel(
            name='SourceBlacklistEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=30, unique=True)),
                ('why', models.TextField()),
                ('added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('who', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WhitelistEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cidr', netfields.fields.CidrAddressField(max_length=43)),
                ('why', models.TextField()),
                ('added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('who', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='blockentry',
            unique_together=set([('block', 'ident')]),
        ),
    ]
