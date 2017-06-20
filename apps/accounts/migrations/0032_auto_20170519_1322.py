# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-19 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0031_auto_20170517_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestinvite',
            name='user_type',
            field=models.CharField(choices=[('BEN', 'Beneficiary'), ('DEV', 'Developer')], default='', max_length=3),
        ),
        migrations.AlterField(
            model_name='requestinvite',
            name='organization',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='aal',
            field=models.CharField(blank=True, choices=[('', 'Undefined'), ('1', 'AAL1'), ('2', 'AAL2'), ('3', 'AAL3')], default='1', help_text='See NIST SP 800 63 B for definitions.', max_length=1, verbose_name='Authenticator Assurance Level'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='ial',
            field=models.CharField(blank=True, choices=[('', 'Undefined'), ('1', 'IAL1'), ('2', 'IAL2'), ('3', 'IAL3')], default='', help_text='See NIST SP 800 63 A for definitions.', max_length=1, verbose_name='Identity Assurance Level'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='loa',
            field=models.CharField(blank=True, choices=[('', 'Undefined'), ('1', 'LOA-1'), ('2', 'LOA-2'), ('3', 'LOA-3'), ('4', 'LOA-4')], default='', help_text='Legacy and Deprecated. Using IAL AAL is recommended.', max_length=1, verbose_name='Level of Assurance'),
        ),
    ]
