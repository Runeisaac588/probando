
from django.urls import path,include
from app_web import views
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
   
    path("",views.contacto, name="Contacto"),
   
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)