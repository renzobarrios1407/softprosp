# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EscenarioBase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_corto', models.CharField(default=b'', max_length=25)),
                ('nombre_largo', models.CharField(default=b'', max_length=50)),
                ('situacion_actual', models.TextField(max_length=100, null=True, blank=True)),
                ('horizonte', models.TextField(max_length=100, null=True, blank=True)),
                ('hipotesis_futuro', models.TextField(max_length=100, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'EscenariosBase',
            },
        ),
        migrations.CreateModel(
            name='EscenarioCompuesto',
            fields=[
                ('id_escenario_comp', models.IntegerField(serialize=False, primary_key=True)),
                ('nombre_compuesto', models.CharField(max_length=50)),
                ('Escenario_base1', models.ForeignKey(related_name='escenariocompuesto_escenario_base1', blank=True, to='smic.EscenarioBase', null=True)),
                ('Escenario_base2', models.ForeignKey(related_name='escenariocompuesto_escenario_base2', blank=True, to='smic.EscenarioBase', null=True)),
            ],
            options={
                'verbose_name_plural': 'Escenarios Compuestos',
            },
        ),
        migrations.CreateModel(
            name='EscenarioPropuesta',
            fields=[
                ('id_Escenario_prop', models.IntegerField(serialize=False, primary_key=True)),
                ('causas', models.TextField(max_length=100, null=True, blank=True)),
                ('consecuencias', models.TextField(max_length=100, null=True, blank=True)),
                ('escenario_base_propuesto', models.ForeignKey(to='smic.EscenarioBase')),
            ],
            options={
                'verbose_name_plural': 'Escenarios Propuestos',
            },
        ),
        migrations.CreateModel(
            name='EvaluacionBase',
            fields=[

                ('id_evaluacion_base', models.IntegerField(serialize=False, primary_key=True)),
                ('calificacion_base', models.DecimalField(default=b'0.0', max_digits=b'10', decimal_places=b'3')),
                ('id_evaluacion_base', models.AutoField(serialize=False, primary_key=True)),
                ('calificacion_base', models.DecimalField(max_digits=3, decimal_places=2, choices=[(b'0', b'0'), (b'0.1', b'0.1'), (b'0.2', b'0.2'), (b'0.3', b'0.3'), (b'0.4', b'0.4'), (b'0.5', b'0.5'), (b'0.6', b'0.6'), (b'0.7', b'0.7'), (b'0.8', b'0.8'), (b'0.9', b'0.9'), (b'1', b'1')])),
                ('comentarios', models.TextField(default=b'', max_length=300)),
                ('id_escenario_base', models.ForeignKey(to='smic.EscenarioBase')),
            ],
            options={
                'verbose_name_plural': 'Evaluaciones Base',
            },
        ),
        migrations.CreateModel(
            name='EvaluacionCompuesta',
            fields=[
                ('id_Evaluacion_comp', models.IntegerField(serialize=False, primary_key=True)),
                ('calificacion_comp', models.DecimalField(default=b'0.0', max_digits=b'10', decimal_places=b'3')),
                ('calificacion_negativa', models.DecimalField(default=b'0.0', max_digits=b'10', decimal_places=b'3')),
                ('id_escenario_comp', models.ForeignKey(to='smic.EscenarioCompuesto')),
            ],
            options={
                'verbose_name_plural': 'Evaluaciones Compuestas',
            },
        ),
        migrations.CreateModel(
            name='Experto',
            fields=[
                ('Id', models.IntegerField(default=0, serialize=False, primary_key=True, blank=True)),
                ('nombre', models.CharField(max_length=25, null=True, blank=True)),
                ('apellidos', models.CharField(max_length=25, null=True, blank=True)),
                ('grupo_experto', models.IntegerField(default=0, null=True, blank=True)),
                ('nivel_influencia', models.IntegerField(default=0, null=True, blank=True)),
                ('Evaluacion_base', models.ForeignKey(default=0, to='smic.EvaluacionBase')),
                ('Evaluacion_compuesta', models.ForeignKey(default=0, to='smic.EvaluacionCompuesta')),
                ('escenario_propuesta', models.ForeignKey(default=0, to='smic.EscenarioPropuesta')),
            ],
        ),
        migrations.CreateModel(
            name='MatrizSimple',
            fields=[
                ('id_matriz', models.IntegerField(serialize=False, primary_key=True)),
                ('tipo_tendencia', models.CharField(max_length=50)),
                ('probabilidad_escenario', models.DecimalField(default=b'0.0', max_digits=b'10', decimal_places=b'3')),
                ('id_escenario_base', models.ForeignKey(to='smic.EscenarioBase')),
            ],
            options={
                'verbose_name_plural': 'Matrices simple',
            },
        ),
        migrations.CreateModel(
            name='Portal',
            fields=[
                ('id_portal', models.IntegerField(serialize=False, primary_key=True)),
                ('id_escenario', models.IntegerField(default=0, null=True, blank=True)),
                ('opinion', models.TextField(max_length=300, null=True, blank=True)),
                ('nivel_influencia', models.IntegerField(default=0, null=True, blank=True)),
                ('experto_anonimo', models.ForeignKey(to='smic.Experto')),
                ('resultado_matriz_simple', models.ForeignKey(to='smic.MatrizSimple')),
            ],
            options={
                'verbose_name_plural': 'Portales',
            },
        ),
    ]
