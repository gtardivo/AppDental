from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from pacientes.models import Pacientes
from pacientes.forms import LoginForms, CadastroForms
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class PacientesList(ListView):
    model = Pacientes
    template_name = "paciente_list.html"


class PacientesCreate(CreateView):
    model = Pacientes
    fields = ["nome", "cpf", "endereco", "cel", "email", "senha"]
    template_name = "paciente_create_form.html"
    success_url = "/pacientes"


class PacientesUpdate(UpdateView):
    model = Pacientes
    fields = ["nome", "cpf", "endereco", "cel", "email", "senha"]
    template_name = "paciente_update_form.html"
    success_url = "/pacientes"


class PacientesDelete(DeleteView):
    model = Pacientes
    template_name = "paciente_delete_form.html"
    success_url = "/pacientes"


def index(request):
    """Tela inicial do site com busca de pacientes"""
    context = {"atributes": None}
    if "buscar" in request.GET:
        queryset_pacientes = Pacientes.objects.all()
        pacientes_pesquisado = request.GET["buscar"]
        atributes = queryset_pacientes.filter(nome__icontains=pacientes_pesquisado)
        context = {"atributes": atributes}
    return render(request, "index.html", context)


def create_user(request):
    """cria um novo usuário de sistema ex. cadastro de secretaria"""
    context = {"form": CadastroForms()}
    if request.method == "POST":
        form = CadastroForms(request.POST)
        if form.is_valid():
            nome = form.cleaned_data["nome"]
            email = form.cleaned_data["email"]
            senha_1 = form.cleaned_data["senha_1"]
            senha_2 = form.cleaned_data["senha_2"]
            if senha_1 == senha_2:
                user = User.objects.create_user(
                    username=nome, email=email, password=senha_1
                )
                user.save()
                return render(request, "index.html")
            else:
                return render(request, "cadastro.html", context)


def change_password(request):
    """Altera a senha do usuário"""
    context = {"form": LoginForms()}
    if request.method == "POST":
        form = LoginForms(request.POST)
        if form.is_valid():
            nome = form.cleaned_data["nome"]
            senha = form.cleaned_data["senha"]
            user = authenticate(username=nome, password=senha)
            if user is not None:
                login(request, user)
                return render(request, "index.html")
            else:
                return render(request, "login.html", context)


def logout_view(request):
    """Faz o logout do usuário"""
    logout(request)
    return render(request, "index.html")


def login(request):
    """Faz o login do usuário"""
    context = {"form": LoginForms()}
    return render(request, "login.html", context)


def cadastro(request):
    """Cria um novo usuário com dados do cadastro"""
    context = {"form": CadastroForms()}
    return render(request, "cadastro.html", context)
