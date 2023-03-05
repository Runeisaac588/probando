
from django.urls import path,include
from .views import Registro, cerrar_sesion, logear

urlpatterns = [
    path("", Registro.as_view(), name="Login"),
    path("cerrar_sesion", cerrar_sesion, name="cerrar_sesion"),
    path("logear", logear, name="iniciar_sesion"),

]

