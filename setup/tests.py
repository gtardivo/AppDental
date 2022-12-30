from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from pacientes.models import Pacientes


class AppDentalTestCase(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('/Users/gtardivo/Desktop/django_tdd/ \
            chromedriver')
        self.pacientes = Pacientes.objects.create(
        nome = "Guilherme",
        cpf = "32124873806",
        endereco = "Q3 CJE Lt4",
        cel = "61-99801-8114"
        )

    def tearDown(self) -> None:
        self.browser.quit()

    def test_busca_paciente(self):
        """
        Teste se o dentista encontra o paciente na busca
        """
        """Verifica na barra de navegacao tem o elemento pacient"""
        home_page = self.browser.get(self.live_server_url + '/')
        """Verifica se retorna um elemento de teste"""
        brand_element = self.browser.find_element(By.CSS_SELECTOR, '.navbar')
        self.assertEqual('Busca Paciente',brand_element.text)
        """  ... """
        buscar_paciente_input = self.browser.find_element(By.CSS_SELECTOR, 'input')
        self.assertEqual(buscar_paciente_input.get_attribute('placeholder'), "Exemplo: André, Felipe...")
        """  ... """
        buscar_paciente_input.send_keys('André')
        self.browser.find_element(By.CSS_SELECTOR, 'form button')
        """  ... """
        pass
