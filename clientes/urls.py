from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/', views.clientes, name='clientes'),
    path('minhas_vacinas/', views.vacina, name='vacina'),
    path('<int:animal_id>', views.ver_animal, name='ver_animal'),
    path('clientes/<int:tutor_id>', views.ver_cliente, name='ver_cliente'),
]
