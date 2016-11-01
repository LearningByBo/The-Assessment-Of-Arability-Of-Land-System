# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('organic_matter', models.IntegerField()),
                ('total_nitrogen', models.IntegerField()),
                ('available_P', models.IntegerField()),
                ('available_K', models.IntegerField()),
            ],
        ),
    ]
