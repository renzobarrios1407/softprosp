# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escenariobase',
            name='hipotesis_futuro',
            field=models.TextField(max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='escenariobase',
            name='horizonte',
            field=models.TextField(max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='escenariobase',
            name='nombre_corto',
            field=models.CharField(default=b'', max_length=300),
        ),
        migrations.AlterField(
            model_name='escenariobase',
            name='nombre_largo',
            field=models.CharField(default=b'', max_length=300),
        ),
        migrations.AlterField(
            model_name='escenariobase',
            name='situacion_actual',
            field=models.TextField(max_length=300, null=True, blank=True),
        ),
    ]
