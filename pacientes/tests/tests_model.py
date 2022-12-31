from django.test import RequestFactory, TestCase
from pacientes.models import Pacientes


class PacientesModelTestCase(TestCase):
    def setUp(self):
        self.pacientes = Pacientes.objects.create(
            nome="Guilherme",
            cpf="32124873806",
            endereco="Q3 CJE Lt4",
            cel="61-99801-8114",
        )

    def test_paciente_cadastro(self):
        self.assertEqual(self.pacientes.nome, "Guilherme")
