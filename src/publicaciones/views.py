from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import Publicacion
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse 

from .forms import PublicarForm, ComentarioForm

class PublicacionesView(ListView):
    template_name = 'publicaciones/publicaciones.html'
    model = Publicacion
    context_object_name = 'publicaciones'

#Clase para crear una piblicacion
class Publicar(CreateView):
    model = Publicacion
    template_name = 'publicaciones/publicar.html'
    form_class = PublicarForm

    def form_valid(self, form):
        nuevo_form = form.save(commit=False)
        nuevo_form.creador_id = self.request.user.id
        return super().form_valid(nuevo_form)

    def get_success_url(self):
        return reverse('publicaciones')

class ModificarPublicacionView(UpdateView):
    model = Publicacion
    template_name = 'publicaciones/modificar-publicacion.html'
    form_class = PublicarForm
    success_url = '../ver-publicaciones'

class EliminarPublicacionView(DeleteView):
    model=Publicacion
    template_name='publicaciones/eliminar-publicacion.html'
    success_url = '../ver-publicaciones'

#Views para ver mas el detalle de una publicacion
class DetallePublicacion(DetailView):
        model=Publicacion
        template_name='publicaciones/detalle.html'
        context_objet_name = 'publicacion'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context ['form'] = ComentarioForm()
            return context
        

        def post(self, request, *args, **kwargs):
             publicacion = self.get_object()
             form = ComentarioForm(request.POST)

             if form.is_valid():
                  comentario = form.save(commit=False)
                  comentario.creador_id = self.request.user.id
                  comentario.publicacion = publicacion
                  comentario.save()
                  return super().get(request)
             else:
                  return super().get(request)