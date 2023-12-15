from django.shortcuts import render

#Vsta basada en Funciones
def index_view(request):
    return render(request,'index.html', {})

def publicaciones_view(request):
    return render(request,'publicaciones.html', {})
