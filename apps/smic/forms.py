from django import forms

from apps.smic.models import EscenarioBase, Experto, EvaluacionBase, EvaluacionCompuesta

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
            'nombre_corto': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_largo': forms.TextInput(attrs={'class':'form-control'}),
            'situacion_actual': forms.TextInput(attrs={'class':'form-control'}),
            'horizonte': forms.TextInput(attrs={'class':'form-control'}),
            'hipotesis_futuro': forms.TextInput(attrs={'class':'form-control'}),
        }

class add_evaluacionBase(forms.ModelForm):

    class Meta:
        model = EvaluacionBase

        fields = [
            'calificacion_base',

        ]

        labels = {
            'calificacion_base': 'calificacion',
        }

        widgets = {
            'calificacion_base': forms.TextInput(attrs={'class':'form-control'}),

        }