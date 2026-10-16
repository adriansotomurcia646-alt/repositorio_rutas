# catalogo/views.py
from django.http import Http404
from django.shortcuts import render
from django.views.generic import TemplateView
from .datos import LIBROS, buscar_libro
from django.http import HttpResponse

def hola(request):
    return HttpResponse("hola desde django")

def inicio(request):
    contexto = {"nombre_sitio": "Catálogo ADSO", "total": len(LIBROS)}
    return render(request, "catalogo/inicio.html", contexto)

def lista_libros(request):
    genero = request.GET.get("genero", "")
    if genero:
        libros = [libro for libro in LIBROS if libro["genero"] == genero]
    else:
        libros = LIBROS
    return render(request, "catalogo/lista.html", {"libros": libros, "genero": genero})

def detalle_libro(request, libro_id):
    libro = buscar_libro(libro_id)
    if libro is None:
        raise Http404("El libro no existe")
    return render(request, "catalogo/detalle.html", {"libro": libro})

from django.http import HttpResponse

def cuadrado(request, numero):
    resultado = numero ** 2
    return HttpResponse(f"El cuadrado de {numero} es {resultado}")

def inicio(request):
    # Calculamos cuántos libros están disponibles y cuántos prestados
    disponibles = sum(1 for libro in LIBROS if libro["disponible"])
    prestados = sum(1 for libro in LIBROS if not libro["disponible"])
    contexto = {
        "nombre_sitio": "Catálogo ADSO",
        "total": len(LIBROS),
        "disponibles": disponibles,
        "prestados": prestados,
    }
    return render(request, "catalogo/inicio.html", contexto)

def lista_autores(request):
    autores_dict = {}
    for libro in LIBROS:
        autor = libro["autor"]
        autores_dict[autor] = autores_dict.get(autor, 0) + 1
    autores_ordenados = sorted(autores_dict.items())

    
    return render(request, "catalogo/autores.html", {"autores": autores_ordenados})

def sugerir_libro(request):
    mensaje = None
    if request.method == "POST":
        titulo_sugerido = request.POST.get("titulo", "").strip()
        
        if not titulo_sugerido:
            mensaje = "Escribe un título"
        else:
            mensaje = f"Gracias, tendremos en cuenta: {titulo_sugerido}"
            
    return render(request, "catalogo/sugerir.html", {"mensaje": mensaje})

class AcercaView(TemplateView):
    template_name = "catalogo/acerca.html"
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["version"] = "1.0"
        return contexto

# --- EJERCICIO ASIGNADO: NOVEDADES (Clase) ---
class NovedadesView(TemplateView):
    template_name = "catalogo/novedades.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        # Filtra libros con año >= 2010 y los ordena del más reciente al más antiguo
        novedades = [l for l in LIBROS if l["anio"] >= 2010]
        novedades.sort(key=lambda x: x["anio"], reverse=True)
        contexto["libros_novedades"] = novedades
        return contexto

class contactoView(TemplateView):
    template_name = "catalogo/contacto.html"