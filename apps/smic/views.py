from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from django.http import HttpResponse
from apps.smic.forms import SmicForm, add_evaluacionBase
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
    return render(request, 'smic/smic_form.html', {'form' : form})

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
    return render(request, 'smic/02 hipotesis.html', {'form':form})

def HipotesisList(request):
    escenario_base = EscenarioBase.objects.all().order_by('id')
    contexto = {'EscenarioBase':escenario_base}
    return render(request, 'smic/03_hipotesis_listas.html', contexto)

def HipotesisCalificacionList(request):
    calificacion = EvaluacionBase.objects

    escenario_base = EscenarioBase.objects.all().order_by('id')
    contexto = {'EscenarioBase':escenario_base}
    return render(request, 'smic/04_calificacion_hipotesis.html', contexto)

def HipotesisCalificacionSelect(request):
    if request.method == 'POST':
        form = add_evaluacionBase(request.POST)
        if form.is_valid():
            form.save()
        return redirect('smic:escenario_simple_calificar')
    else:
        form = add_evaluacionBase()

    return render(request, 'smic/04_calificacion_hipotesis.html', {'form': form})

def EvaluacionBase_list(request):
    evaluacion_base = EvaluacionBase.objects.all().order_by('id')
    contexto = {'EvaluacionBase':evaluacion_base}
    return render(request, 'smic/03_hipotesis_listas.html', contexto)

class HipotesisPrueba(ListView):
    model = EscenarioBase
    template_name = 'smic/03_hipotesis_listas.html'
    form_class = SmicForm


