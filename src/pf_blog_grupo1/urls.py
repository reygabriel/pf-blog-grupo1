from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name='index'),
    path('publicaciones/', views.publicaciones_view, name='publicaciones')

    #Includes creados
    #path('publicaciones/', include('publicaciones.urls'))
]
