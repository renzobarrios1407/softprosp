from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from django.http import HttpResponse
from apps.smic.forms import SmicForm

from apps.smic.forms import SmicForm, EvaluacionBase_Form, EvaluacionCompuesta_Form, EscenarioCompuesto_form
from apps.smic.models import EscenarioBase, EvaluacionBase

# Create your views here.

def index(request):
    return render(request, 'smic/Index.html')

def smic_view(request):
    if request.method == 'POST':
        form = SmicForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('smic:index')
    else:
        form = SmicForm()
    return render(request, 'smic/smic_form.html', {'form': form})

def escenario_base(request):
    return render(request, 'smic/02 hipotesis.html')

def EscenarioBase_list(request):
    escenario_base = EscenarioBase.objects.all().order_by('id')
    contexto = {'EscenarioBase':escenario_base}
    return render(request, 'smic/smic_list.html', contexto)

def EscenarioBase_edit(request, id_EscenarioBase):
    escenario_base = EscenarioBase.objects.get(id=id_EscenarioBase)
    if request.method == 'GET':
        form = SmicForm(instance=escenario_base)
    else:
        form = SmicForm(request.POST, instance=escenario_base)
        if form.is_valid():
            form.save()
        return redirect('smic:escenario_lista')
    return render(request, 'smic/smic_form.html', {'form':form})

def EscenarioBase_Delete (request, id_EscenarioBase):
    escenario = EscenarioBase.objects.get(id=id_EscenarioBase)
    if request.method == 'POST':
        escenario.delete()
        return redirect('smic:escenario_lista')
    return render(request, 'smic/smic_delete.html', {'escenario':escenario})



def HipotesisCreate(request):
    if request.method == 'POST':
        form = SmicForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('smic:escenario_crear_listar')
    else:
        form = SmicForm()
    context = {'form':form}
    return render(request, 'smic/02 hipotesis.html', context)

def HipotesisList(request):
    escenario_base = EscenarioBase.objects.all().order_by('id')
    contexto = {'EscenarioBase':escenario_base}
    return render(request, 'smic/03_hipotesis_listas.html', contexto)


def HipotesisCalificacionList(request):
    escenario_base = EscenarioBase.objects.all().order_by('id')
    contexto = {'EscenarioBase':escenario_base}
    return render(request, 'smic/04_calificacion_hipotesis.html', contexto)


def HipotesisCalificacionSimple(request):
    if request.method == 'POST':
        form_evaluacion = EvaluacionBase_Form(request.POST)
        if form_evaluacion.is_valid():
            form_evaluacion.save()
        return redirect('smic:escenario_simple_calificar')
    else:
        form_evaluacion = EvaluacionBase_Form()

    contexto = {'form_evaluacion': form_evaluacion}
    return render(request, 'smic/04_calificacion_hipotesis.html', contexto)

def HipotesisCalificacionCompuesta(request):
    if request.method == 'POST':
        form = EvaluacionCompuesta_Form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('smic:escenario_compuesto_calificar')
    else:
        form = EvaluacionCompuesta_Form()

    context = {'evaluacion_compuesta':form}
    return render(request, 'smic/05_calificacion_compuesta.html', context)

def Hipotesis_Compuesta_Create(request):
    if request.method == 'POST':
        escenario_compuesto = EscenarioCompuesto_form(request.POST)
        if escenario_compuesto.is_valid():
            escenario_compuesto.save()
        return redirect('smic:escenario_compuesto_crear')
    else:
        escenario_compuesto = EscenarioCompuesto_form()
    escenario_simple = EscenarioBase.objects.all().order_by('id')
    context = {'form':escenario_compuesto, 'escenario_simple':escenario_simple}
    return render(request, 'smic/06_hipotesis_compuestas.html', context)


def EvaluacionBase_list(request):
    evaluacion_base = EvaluacionBase.objects.all().order_by('id')
    contexto = {'EvaluacionBase':evaluacion_base}
    return render(request, 'smic/03_hipotesis_listas.html', contexto)

class HipotesisPrueba(ListView):
    model = EscenarioBase
    template_name = 'smic/03_hipotesis_listas.html'
    form_class = SmicForm


