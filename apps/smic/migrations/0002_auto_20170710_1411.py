# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluacionbase',
            name='calificacion_base',
            field=models.CharField(max_length=11, choices=[(b'a', b'a'), (b'b', b'b'), (b'c', b'c'), (b'd', b'd'), (b'e', b'e'), (b'f', b'f'), (b'g', b'g'), (b'h', b'h'), (b'i', b'i'), (b'j', b'j'), (b'k', b'k')]),
        ),
    ]
