#coding:utf-8
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'softprosp.settings')

import django
django.setup()

from apps.smic.models import EscenarioBase


def populate():
    escenario_1 =[
        'desesion universitaria',
        'desercion universitaria en el programa de ingenieria de sistemas',
        'los estudiantes de primero, segundo y tercer semestre muestran una desercion alta debido a su mal desempeno en la carrera',
        'se aspira que al ano 2020 se obtenga el 0% de desercion en el programa',
        'como mejor alternativa, se disctaran cursos para el refuerzo del conocimiento de las asignaturas y poder ganar los examenes pertinentes',
    ]

    escenario_2 = [
        'soluciones a caidas de energia electrica en el sector del caribe Colombiano',
        'solucion para la caida de energia electrica en el sector del caribe colombiano, con el fin de erradicar la mala calidad del servicio de luz y moderar su uso en los hogares',
        '7 de cada 10 hogares sufren de racionalizacion de luz, por ende eso baja la calidad de vida de las personas haciendolas mas propensas a enfermarse u mostrar mal desempeño en sus labores diaras',
        'mediante el decreto 1446 de 2017 se abriran nuevas alternativas para el servicio electrico de la cosa, para que se puedan implementar nuevas ayudas en los hogares colombianos',
        'al aplicar la medida de solucion, los hogares colombianos tendran un beneficio en su vida diaria y se podra corregir las irregularidades que ha tenido la empresa anteiror',
    ]




    # if you want to add more catergories or pages, add them to the dictionaries above

    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category
    # if you are using Python 2.x then use cats.iteritems() see
    # http://docs.quantifiedcode.com/python-anti-patterns/readability/not_using_items_to_iterate_over_a_dictionary.html
    # for more information about using items() and how to iterate over a dictionary properly

    # Using the .items returns the key and the value. In this case the key is "Python", "Django" or "Other Frameworks" and the value (cat_data) is the corresponding dictionary in cats.


        # c = add_cat(cat)
        # Updated the population script to pass through the specific values for views and likes
    c = add_escenario(escenario_1[0], escenario_1[1], escenario_1[2], escenario_1[3], escenario_1[4])
    c = add_escenario(escenario_2[0], escenario_2[1], escenario_2[2], escenario_2[3], escenario_2[4])

    # Print out what we have added to the user.
    for c in EscenarioBase.objects.all():
           print("- {0}".format(str(c)))


def add_escenario(nom_corto,nom_largo, sit_act, hor, hip_fut):

    esc = EscenarioBase.objects.get_or_create(nombre_corto=nom_corto)[0]
    esc.nombre_largo = nom_largo
    esc.situacion_actual = sit_act
    esc.horizonte = hor
    esc.hipotesis_futuro = hip_fut
    # we need to save the changes we made!!
    esc.save()
    return esc




# Start execution here!
if __name__ == '__main__':
    print("Starting the smic population script...")
    populate()