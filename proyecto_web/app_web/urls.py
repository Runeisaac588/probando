
from django.urls import path,include
from app_web import views

urlpatterns = [
    path("home",views.home, name="Home"),
    path("servicios",views.servicio, name="Servicios"),
    path("tienda",views.tienda, name="Tienda"),
    path("blog",views.blog, name="Blog"),
    path("contacto",views.contacto, name="Contacto"),
]
