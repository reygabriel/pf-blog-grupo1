from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Publicacion, Comentario, Categoria
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import ColaboradorMixin, CreadorMixin

from .forms import PublicarForm, ComentarioForm

class PublicacionesView(ListView):
    template_name = 'publicaciones/publicaciones.html'
    model = Publicacion
    context_object_name = 'publicaciones'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context
    
    
    def get_queryset(self):
        queryset = super().get_queryset()

        categoria_seleccionada = self.request.GET.get('categoria')

        if categoria_seleccionada:
            queryset = queryset.filter(categoria = categoria_seleccionada)
            
        
    #Orden
        orden = self.request.GET.get('orderby')
        if orden:
            if orden == 'fecha_asc':
                queryset = queryset.order_by('fecha')
            elif orden == 'fecha_desc':
                queryset = queryset.order_by('-fecha')
            elif orden == 'alf_asc':
                orden = queryset.order_by('titulo')
            elif orden == 'alf_desc':
                queryset = queryset.order_by('-titulo')
        
        return queryset
 

#Clase para crear una piblicacion
class Publicar(LoginRequiredMixin, ColaboradorMixin, CreateView):
    model = Publicacion
    template_name = 'publicaciones/publicar.html'
    form_class = PublicarForm

    def form_valid(self, form):
        nuevo_form = form.save(commit=False)
        nuevo_form.creador_id = self.request.user.id
        return super().form_valid(nuevo_form)

    def get_success_url(self):
        return reverse('publicaciones')

class ModificarPublicacionView(CreadorMixin, UpdateView):
    model = Publicacion
    template_name = 'publicaciones/modificar-publicacion.html'
    form_class = PublicarForm
    success_url = '../ver-publicaciones'

class EliminarPublicacionView(CreadorMixin, DeleteView):
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
            if not self.request.user.is_authenticated:
                return redirect('login')
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

class BorrarComentarioView(CreadorMixin, DeleteView):
    model=Comentario
    template_name='comentarios/borrar-comentario.html'
    
    def get_success_url(self):
        return reverse('detalle-publicacion', args=[self.object.publicacion.id])

class EditarComentarioView(CreadorMixin, UpdateView):
    model = Comentario
    template_name = 'comentarios/editar-comentario.html'
    form_class = ComentarioForm

    def get_success_url(self):
        return reverse('detalle-publicacion', args=[self.object.publicacion.id])