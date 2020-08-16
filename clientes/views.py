from django.shortcuts import render, get_object_or_404
from .models import Animal, Vacina, Tutor, Consulta, Cirurgia


def index(request):
    animais = Animal.objects.all()
    clientes = Tutor.objects.all()
    return render(request, 'clientes/index.html', {
        'animais': animais,
        'clientes': clientes
    })

def clientes(request):
    clientes = Tutor.objects.all()
    return render(request, 'clientes/clientes.html', {
        'clientes': clientes,
    })

def ver_animal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    clientes = Tutor.objects.all()
    return render(request, 'clientes/ver_animal.html', {
        'clientes': clientes,
        'animal': animal,
    })

def ver_cliente(request, tutor_id):
    tutor = get_object_or_404(Tutor, id=tutor_id)
    animais = Animal.objects.all()
    return render(request, 'clientes/ver_cliente.html', {
        'animais': animais,
        'tutor': tutor,
    })

def vacina(request):
    vacinas = Vacina.objects.all()
    return render(request, 'clientes/minhas_vacinas.html', {
        'vacinas': vacinas,
    })

def consulta(request):
    consultas = Consulta.objects.all()
    return render(request, 'clientes/minhas_consultas.html', {
        'consultas': consultas,
    })

def cirurgia(request):
    cirurgias = Cirurgia.objects.all()
    return render(request, 'clientes/minhas_cirurgias.html', {
        'cirurgias': cirurgias,
    })
