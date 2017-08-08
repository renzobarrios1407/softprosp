from django.db import models

from apps.smic.Choices import valores_calificacion


# Create your models here.

class Experto(models.Model):
    """experto encargado de estar en el proyecto"""
    Id = models.IntegerField(default=0, blank=True, null=False,primary_key=True)
    nombre = models.CharField(max_length=25,blank= True, null=True)
    apellidos = models.CharField(max_length=25,blank= True, null=True)
    grupo_experto = models.IntegerField(default=0, blank=True, null=True)
    nivel_influencia = models.IntegerField(default=0, blank=True, null=True)
    """llaves foraneas"""
    escenario_propuesta = models.ForeignKey('EscenarioPropuesta', on_delete=models.CASCADE, default=0)
    Evaluacion_base = models.ForeignKey('EvaluacionBase', on_delete=models.CASCADE, default=0)
    Evaluacion_compuesta = models.ForeignKey('EvaluacionCompuesta', on_delete=models.CASCADE, default=0)

    def __unicode__(self):
        return '{}'.format(self.Id)

class EscenarioBase(models.Model):

    nombre_corto = models.CharField(max_length=300, blank=False, null=False, default="")
    nombre_largo = models.CharField(max_length=300, blank=False, null=False, default="")
    situacion_actual = models.TextField(max_length=300,blank=True,null=True)
    horizonte = models.TextField(max_length=300,blank=True,null=True)
    hipotesis_futuro = models.TextField(max_length=300,blank=True,null=True)

    class Meta:
        verbose_name_plural = 'EscenariosBase'

    def __unicode__(self):
        return '{}'.format(self.nombre_corto)

class EscenarioCompuesto(models.Model):
    id_escenario_comp = models.IntegerField(primary_key=True,null=False, blank=False)
    nombre_compuesto = models.CharField(max_length=50, blank=False, null=False)
    """Llaves Foraneas"""
    Escenario_base1 = models.ForeignKey('EscenarioBase', null=True, blank=True, on_delete=models.CASCADE,
                                        related_name='%(class)s_escenario_base1')
    Escenario_base2 = models.ForeignKey('EscenarioBase', null=True, blank=True, on_delete=models.CASCADE,
                                        related_name='%(class)s_escenario_base2')

    class Meta:
        verbose_name_plural = 'Escenarios Compuestos'

    def __unicode__(self):
        return self.id_base

class EvaluacionCompuesta(models.Model):
    id_Evaluacion_comp = models.IntegerField(primary_key=True, null=False, blank=False)
    calificacion_comp = models.DecimalField(max_digits='10', decimal_places='3', default='0.0')
    calificacion_negativa = models.DecimalField(max_digits='10', decimal_places='3', default='0.0')
    """Llaves foraneas"""
    id_escenario_comp = models.ForeignKey('EscenarioCompuesto', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Evaluaciones Compuestas'

    def __unicode__(self):
        return self.id_Evaluacion_comp

class EvaluacionBase(models.Model):
    id_evaluacion_base = models.AutoField(primary_key=True, null=False, blank=False)
    calificacion_base = models.DecimalField(decimal_places=2, max_digits=3)
    comentarios = models.TextField(null=False, blank=False, default="", max_length=300)

    """Llaves Foraneas"""
    id_escenario_base = models.ForeignKey('EscenarioBase', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Evaluaciones Base'

    def __unicode__(self):
        return self.id_evaluacion_base

class EscenarioPropuesta(models.Model):
    id_Escenario_prop = models.IntegerField(primary_key=True, null=False, blank=False)
    causas = models.TextField(max_length=100,blank=True,null=True)
    consecuencias = models.TextField(max_length=100,blank=True,null=True)
    """Llaves Foraneas"""
    escenario_base_propuesto = models.ForeignKey('EscenarioBase', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Escenarios Propuestos'

    def __unicode__(self):
        return self.id_Escenario_prop

class Portal(models.Model):
    id_portal = models.IntegerField(primary_key=True, null=False, blank=False)
    id_escenario = models.IntegerField(default=0, blank=True, null=True)
    opinion = models.TextField(max_length=300,blank=True,null=True)
    nivel_influencia = models.IntegerField(default=0, blank=True, null=True)
    """Llaves Foraneas"""
    experto_anonimo = models.ForeignKey('Experto', on_delete=models.CASCADE)
    resultado_matriz_simple = models.ForeignKey('MatrizSimple', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Portales'

    def __unicode__(self):
        return self.id_portal

class MatrizSimple(models.Model):
    id_matriz = models.IntegerField(primary_key=True, null=False, blank=False)
    tipo_tendencia = models.CharField(max_length=50, blank=False, null=False)
    probabilidad_escenario = models.DecimalField(max_digits='10', decimal_places='3', default='0.0')
    """Llaves Foraneas"""
    id_escenario_base = models.ForeignKey('EscenarioBase', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Matrices simple'

    def __unicode__(self):
        return self.id_matriz