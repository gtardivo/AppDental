from django.urls import path
from pacientes.views import index, cadastro, login, PacientesList, PacientesCreate, PacientesUpdate, PacientesDelete


urlpatterns = [
    path('', index, name='index'),
    path('paciente', PacientesList.as_view(), name='pacienteList'),
    path('paciente/create', PacientesCreate.as_view(), name='pacienteCreate'),
    path('paciente/update/<int:pk>', PacientesUpdate.as_view(), name='pacienteUpdate'),
    path('paciente/delete/<int:pk>', PacientesDelete.as_view(), name='pacienteDelete'),
    path('/cadastro', cadastro, name='cadastro'),
    path('/login', login, name='login'),
]
