# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-11-11 17:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0023_auto_20161102_2039'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegisterCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=150)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('sent', models.BooleanField(default=False, editable=False)),
                ('used', models.BooleanField(default=False)),
                ('resend', models.BooleanField(default=False, help_text=b'Check to resend')),
                ('added', models.DateField(auto_now_add=True)),
                ('sender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='userregisterinvitation',
            name='sender',
        ),
        migrations.AlterModelOptions(
            name='invitation',
            options={'verbose_name': 'Developer Invitation'},
        ),
        migrations.DeleteModel(
            name='UserRegisterInvitation',
        ),
    ]
