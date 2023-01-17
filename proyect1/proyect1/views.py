from django.http import HttpResponse
from datetime import date
import datetime
from string import Template
from django.template import Template,Context
from django.template import loader
from django.shortcuts import render


def adios(request):
     return HttpResponse("adios")


def dameFecha(request):
     fecha_actual =datetime.datetime.now()
     documento ="""<html> 
     <body>
     <h1> 
     fecha y hora actual %s
     </h1>
     </body>
     </html>
     """ % fecha_actual
     return HttpResponse(documento)
    

def calculaEdad (request,edad,year):
     
    
     periodo=year-2019
     edadFutura = edad+periodo
     documento= """
     <html>
     <body>
     <h2>En el año %s tendras %s años</h2>
     </body>
     </html>
     
     """%(year,edadFutura)
     return HttpResponse(documento)
     return 

class persona(object):
     def __init__(self,nombre, apellido):
          self.nombre=nombre
          self.apellido=apellido

def saludo(request):
     
     p1=persona("Adan","arrieta")
     nombre="juan"
     apellido="Diaz"
     ahora=datetime.datetime.now()
    # doc_externo = open(r"C:\Users\adani\Desktop\cursoDjango\proyect1\proyect1\plantillas\index.html")
     temas=["plantillas","Bucles","condicionales","tipos de datos","recursividad"]
     #temas=[]
     #plt= Template(doc_externo.read())
     #doc_externo.close()
     #uso de cargadores
     doc_externo=loader.get_template('index.html')
 
     #documento=doc_externo.render({"nombre_persona":nombre,"apellido_persona": apellido,"Fecha_hoy":ahora, "alumno_es": [p1.nombre,"y se apellida",p1.apelldio],"temas_curso":temas})
     
     return render(request, "index.html",{"nombre_persona":nombre,"apellido_persona": apellido,"Fecha_hoy":ahora, "alumno_es": p1.nombre,"y se apellida":p1.apellido,"temas_curso":temas})

def cursoC (request):
     
     ahora=datetime.datetime.now()
     return render(request,"CursoC.html",{"Fecha_hoy":ahora})
     

def cursoCSS (request):
     
     ahora=datetime.datetime.now()
     return render(request,"cursoCss.html",{"Fecha_hoy":ahora})

