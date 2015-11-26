# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='headimage',
            field=models.ImageField(default=datetime.datetime(2015, 11, 26, 9, 22, 36, 741486, tzinfo=utc), upload_to=''),
            preserve_default=False,
        ),
    ]
