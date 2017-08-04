from django.conf.urls import url, include


from apps.smic.views import index, smic_view, escenario_base, EscenarioBase_list, EscenarioBase_edit, EscenarioBase_Delete, HipotesisCreate, HipotesisPrueba, HipotesisList, HipotesisCalificacionList

from apps.smic.views import index, smic_view, escenario_base, EscenarioBase_list, EscenarioBase_edit, EscenarioBase_Delete, HipotesisCreate, HipotesisPrueba, HipotesisList, HipotesisCalificacionSimple, HipotesisCalificacionCompuesta



urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', smic_view, name='escenario_crear'),
    url(r'^base$', escenario_base, name='escenario_base'),
    url(r'^listar$', EscenarioBase_list, name='escenario_lista'),
    url(r'^editar/(?P<id_EscenarioBase>\d+)/$', EscenarioBase_edit, name='escenario_editar'),
    url(r'^borrar/(?P<id_EscenarioBase>\d+)/$', EscenarioBase_Delete, name='escenario_borrar'),

    url(r'^hip_nuevo$', HipotesisCreate, name='escenario_crear_listar'),
    url(r'^hip_lista$', HipotesisList, name='escenario_listar'),
    url(r'^hip_cal1$', HipotesisCalificacionList, name='escenario_simple_calificar'),
    url(r'^hip_cal1$', HipotesisCalificacionSimple, name='escenario_simple_calificar'),
    url(r'^hip_cal2$', HipotesisCalificacionCompuesta, name='escenario_compuesto_calificar'),


    url(r'^hip_simple', HipotesisPrueba.as_view(), name='escenario_simple')


]