from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project/', views.project, name='project'),
    path('sponsorship/', views.sponsorship, name='sponsorship'),
    path('success/', views.success, name='success'),
    path('contact/', views.contact, name='contact'),
    path('cadastrar_animal/', views.cadastrar_animal, name='cadastrar_animal'),
    path('painel/', views.painel, name='painel'),
    path('editar-animal/<int:id>/', views.editar_animal, name='editar_animal'),
]
