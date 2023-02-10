
from django.urls import path,include
from app_web import views
from django.conf import settings
from django.conf.urls.static import static
from servicios import views
urlpatterns = [
   
    path("",views.servicio, name="Servicios"),
   
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)