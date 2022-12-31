from django.test import TestCase, RequestFactory
from django.urls import reverse
from pacientes.views import index


class PacientesURLsTestCase(TestCase):
    def setUp(self):
        """ "SetUp inicial de requestsHttp para utilizacao no Reverse"""
        self.factory = RequestFactory()

    def test_url_view_index(self):
        """ "Teste Home View de Pacientes"""
        request = self.factory.get("/")
        with self.assertTemplateUsed("index.html"):
            response = index(request)
            self.assertEqual(response.status_code, 200)
