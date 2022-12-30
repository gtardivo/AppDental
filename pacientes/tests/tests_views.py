from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet
from pacientes.models import Pacientes


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.pacientes = Pacientes.objects.create(
            nome = "Guilherme",
            cpf = "32124873806",
            endereco = "Q3 CJE Lt4",
            cel = "61-99801-8114"
        )

    def test_index_return_atributes(self):
        """"Teste"""
        response = self.client.get('/',
        {'buscar':'Guilherme'}
        )
        atributos_paciente = response.context['atributes']
        self.assertIs(type(response.context['atributes']), QuerySet)
        self.assertAlmostEqual(atributos_paciente[0].nome, 'Guilherme')
