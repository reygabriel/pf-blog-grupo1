from django.shortcuts import render
from .models import Publicacion
from django.views.generic import ListView


class PublicacionesView(ListView):
    template_name = 'publicaciones.html'
    model = Publicacion
    context_object_name = 'publicaciones'



