# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('name', models.CharField(max_length=256, verbose_name='name')),
                ('headers_top', models.PositiveSmallIntegerField(default=1, verbose_name='top')),
                ('headers_left', models.PositiveSmallIntegerField(default=0, verbose_name='left')),
                ('headers_bottom', models.PositiveSmallIntegerField(default=0, verbose_name='bottom')),
                ('table_data', models.TextField(verbose_name='table data')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
