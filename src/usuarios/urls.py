from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('registrarse/', views.RegistrarseView.as_view(), name='registrarse'),
    path('login/', LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('mi-perfil/', views.mi_perfil_view, name='mi-perfil'),
    path('editar-perfil/<int:pk>', views.EditarPerfilView.as_view(), name='editar-perfil'),
]