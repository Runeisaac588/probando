import re
from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):

    return render(request,"app_web/home.html")

def servicio(request):

     return render(request,"app_web/servicios.html")


def tienda(request):

     return render(request,"app_web/tienda.html")


def blog(request):

    return render(request,"app_web/blog.html")


def contacto(request):

    return render(request,"app_web/contacto.html")
