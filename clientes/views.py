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
    animais = Animal.objects.all()
    return render(request, 'clientes/minhas_vacinas.html', {
        'vacinas': vacinas,
        'animais': animais,
    })

def consulta(request):
    consultas = Consulta.objects.all()
    animais = Animal.objects.all()    
    return render(request, 'clientes/minhas_consultas.html', {
        'consultas': consultas,
        'animais': animais,
    })

def cirurgia(request):
    cirurgias = Cirurgia.objects.all()
    animais = Animal.objects.all()    
    return render(request, 'clientes/minhas_cirurgias.html', {
        'cirurgias': cirurgias,
        'animais': animais,
    })

def ver_vacina(request, vacina_id):
    vacina = get_object_or_404(Vacina, id=vacina_id)
    animais = Animal.objects.all()
    return render(request, 'clientes/ver_vacina.html', {
        'animais': animais,
        'vacina': vacina,
    })

def ver_consulta(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)
    animais = Animal.objects.all()
    return render(request, 'clientes/ver_consulta.html', {
        'animais': animais,
        'consulta': consulta,
    })

def ver_cirurgia(request, cirurgia_id):
    cirurgia = get_object_or_404(Cirurgia, id=cirurgia_id)
    animais = Animal.objects.all()
    return render(request, 'clientes/ver_cirurgia.html', {
        'animais': animais,
        'cirurgia': cirurgia,
    })