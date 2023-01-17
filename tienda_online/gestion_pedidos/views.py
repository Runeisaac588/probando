from django.shortcuts import render,HttpResponse
from gestion_pedidos.models import articulo
from django.core.mail import send_mail
from django.conf import settings
from gestion_pedidos.forms import formulario_contacto
# Create your views here.

def busqueda_productos(request):
    return render(request,'busqueda_productos.html')

def buscar(request):
    if request.GET["prd"]:
        
     #mensaje='Articulo buscado: %r'%request.GET["prd"]
     producto=request.GET["prd"]
     
     if len(producto)>20:
         mensaje="Texto de busqueda demasiado largo"
     else:
        
      articulos= articulo.objects.filter(nombre__icontains=producto)
      return render(request,"resultados_busqueda.html",{"articulos":articulos,"query":producto})
    else:
     mensaje="no introdujiste nada"
     
    return HttpResponse(mensaje)
    
def contacto(request):
    if request.method =="POST":
        miForm=formulario_contacto(request.POST)
        
        if miForm.is_valid():
            infForm=miForm.cleaned_data
            
            send_mail(infForm['asunto'],infForm['mensaje'],infForm.get('email','adanisakito@gmail.com'),['adanisakito@hotmail.com'],)
            
            return render(request,"gracias.html")
    else:
        miForm=formulario_contacto()
            
    return render(request,"formulario_contacto.html",{"form": miForm})
        
        #message=request.POST["mensaje"] +" "+ request.POST["email"]
        #subject=request.POST["asunto"]
        #email_from=settings.EMAIL_HOST_USER
        #recipient_list=['adanisakito@hotmail.com']
        #send_mail(subject,message ,email_from, recipient_list)
  
        #return render(request,"gracias.html")
        
   # return render(request,"contacto.html")