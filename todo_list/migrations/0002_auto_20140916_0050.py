# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]
