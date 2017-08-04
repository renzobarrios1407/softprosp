#coding:utf-8
from django import forms


from apps.smic.models import EscenarioBase, Experto, EvaluacionBase, EvaluacionCompuesta
from apps.smic.models import EscenarioBase, Experto, EvaluacionBase, EvaluacionCompuesta, EscenarioCompuesto
from apps.smic.Choices import valores_calificacion


class SmicForm(forms.ModelForm):

    class Meta:
        model = EscenarioBase

        fields = [
            'nombre_corto',
            'nombre_largo',
            'situacion_actual',
            'horizonte',
            'hipotesis_futuro',
        ]

        labels = {
            'nombre_corto': 'Nombre Corto',
            'nombre_largo': 'Nombre Largo',
            'situacion_actual': 'Descripcion escenario actual (situacion actual)',
            'horizonte': 'Descripcion como se lograria llegar (Horizonte)',
            'hipotesis_futuro': 'Descripcion de lo que debe suceder (hipotesis futuro)',
        }

        widgets = {
            'nombre_corto': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_largo': forms.TextInput(attrs={'class': 'form-control'}),
            'situacion_actual': forms.TextInput(attrs={'class': 'form-control'}),
            'horizonte': forms.TextInput(attrs={'class': 'form-control'}),
            'hipotesis_futuro': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EvaluacionBase_Form(forms.ModelForm):

    class Meta:
        model = EvaluacionBase

        fields = [
            'calificacion_base',
            'id_escenario_base',
            'comentarios',

        ]

        labels = {
            'calificacion_base': 'Calificacion',
            'id_escenario_base': 'Escenario',
            'comentarios': 'comentario',
        }

        widgets = {
            'calificacion_base': forms.Select(choices=valores_calificacion),
            'id_escenario_base': forms.Select(),
            'comentario': forms.TextInput(),
        }

class EvaluacionCompuesta_Form(forms.ModelForm):
    class Meta:
        model = EvaluacionCompuesta

        fields = {
            'calificacion_comp',
            'calificacion_negativa',
            'id_escenario_comp',

        }

        labels = {
            'calificacion_comp': 'Calificacion_compuesta',
            'calificacion_negativa': 'calificacion_negativa',
            'id_escenario_comp': 'escenario_compuesto',
        }

        widgets = {

            'calificacion_comp': forms.Select(choices=valores_calificacion),
            'calificacion_negativa': forms.Select(choices=valores_calificacion),


        }