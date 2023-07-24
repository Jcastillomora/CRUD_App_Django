from django.test import TestCase
from laboratorio.models import Laboratorio
from django.urls import reverse

# Create your tests here.
class LaboratorioModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Crea un laboratorio para usar en todas las pruebas
        Laboratorio.objects.create(nombre='Laboratorio de Prueba', ciudad='Temuco', pais='Chile')

    def test_datos_en_base_de_datos(self):
        laboratorio = Laboratorio.objects.get(nombre='Laboratorio de Prueba')
        self.assertEqual(laboratorio.ciudad, 'Temuco')
        self.assertEqual(laboratorio.pais, 'Chile')
        # Agrega más aserciones según los campos de tu modelo que desees verificar

class LaboratorioURLTest(TestCase):

    def test_respuesta_http_200(self):
        url = reverse('mostrar_lab_view')  # Reemplaza 'nombre_de_la_url' con el nombre de la URL de tu vista
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

class LaboratorioTemplateTest(TestCase):

    def test_respuesta_http_200_y_plantilla_correcta(self):
        url = reverse('mostrar_lab_view')  # Reemplaza 'nombre_de_la_url' con el nombre de la URL de tu vista
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mostrar.html')  # Reemplaza 'nombre_de_la_plantilla.html' con el nombre de tu plantilla
        self.assertContains(response, '<h2 class="text-center">Información de Laboratorios</h2> ')  # Reemplaza 'Texto esperado en la plantilla' con el contenido HTML esperado en tu plantilla
        # Puedes agregar más aserciones según lo que desees verificar en tu plantilla