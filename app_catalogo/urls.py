from django.urls import path
from . import views

app_name = "catalogo"

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("libros/", views.lista_libros, name="lista_libros"),
    path("libros/<int:libro_id>/", views.detalle_libro, name="detalle_libro"),
    path("acerca/", views.AcercaView.as_view(), name="acerca"),
    path("novedades/", views.NovedadesView.as_view(), name="novedades"), 
    path("hola/", views.hola, name="hola"),
    path("cuadrado/<int:numero>/", views.cuadrado, name="cuadrado"),
    path("contacto/", views.contactoView.as_view(), name="contacto"),
    path("autores/", views.lista_autores, name="autores"),
    path("sugerir/", views.sugerir_libro, name="sugerir"),
] 