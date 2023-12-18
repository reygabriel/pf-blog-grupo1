from django.shortcuts import render
from .models import Publicacion
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
 

from .forms import PublicarForm

class PublicacionesView(ListView):
    template_name = 'publicaciones/publicaciones.html'
    model = Publicacion
    context_object_name = 'publicaciones'


class Publicar(CreateView):
    model = Publicacion
    template_name = 'publicaciones/publicar.html'
    form_class = PublicarForm

class ModificarPublicacionView(UpdateView):
    model = Publicacion
    template_name = 'publicaciones/modificar-publicacion.html'
    form_class = PublicarForm
    success_url = '../ver-publicaciones'

class EliminarPublicacionView(DeleteView):
    model=Publicacion
    template_name='publicaciones/eliminar-publicacion.html'
    success_url = '../ver-publicaciones'
