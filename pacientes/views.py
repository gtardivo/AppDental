from django.shortcuts import render
from pacientes.models import Pacientes


def index(request):
    context = {'atributes' : None}

    if 'buscar' in request.GET:
        pacientes = Pacientes.objects.all()
        pacientes_pesquisado = request.GET['buscar']
        atributes = pacientes.filter(nome__icontains = pacientes_pesquisado)
        context = {'atributes': atributes}
    return render(request, 'index.html', context)
