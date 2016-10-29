# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prognoz', '0032_remove_prognozdata_dist_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='prognozdata',
            name='distance_pr',
            field=models.SmallIntegerField(default=1, verbose_name=b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd1\x8f\xd0\xb7\xd0\xba\xd0\xb0'),
            preserve_default=False,
        ),
    ]
