from django.shortcuts import render

#Vista basada en Funciones
def index_view(request):
    return render(request,'index.html', {})

def contacto_view(request):
    return render(request, 'contacto.html', {})