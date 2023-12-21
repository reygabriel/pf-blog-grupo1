from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name='index'),
    path('contacto/', views.contacto_view, name='contacto'),

    #Includes creados
    path('publicaciones/', include('publicaciones.urls')),
    path('usuarios/', include('usuarios.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)