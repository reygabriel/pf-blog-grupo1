from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name='index'),

    #Includes creados
    path('publicaciones/', include('publicaciones.urls')),
]
