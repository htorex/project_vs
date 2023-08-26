from django.test import TestCase

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from vs.forms import Registerform

class RegisterViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('register')  # Asegúrate de que 'register' sea el nombre de la URL en tu archivo urls.py

    def test_register_user(self):
        response = self.client.post(self.url, {
            'username': 'testuser',
            'email': 'test@example.com',
            #'rut': '12345678',
            'password': 'testpassword',
        })

        # Verificar que la respuesta tenga el estado 302 (redirección)
        self.assertEqual(response.status_code, 302)

        # Verificar que el usuario haya sido creado en la base de datos
        self.assertTrue(User.objects.filter(username='testuser').exists())

        # Verificar que el usuario esté autenticado después de registrar
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_register_authenticated_user(self):
        # Simular un usuario autenticado
        self.client.login(username='existinguser', password='password')

        response = self.client.get(self.url)

        # Verificar que el usuario autenticado sea redirigido
        self.assertEqual(response.status_code, 302)

    def test_register_invalid_form(self):
        response = self.client.post(self.url, {
            'username': 'testuser',
            'email': 'invalid_email',  # Provoca un error de validación
            'rut': '12345678',
            'password': 'testpassword',
        })

        # Verificar que el formulario no es válido y no se ha creado un usuario
        self.assertFalse(form.is_valid())
        self.assertFalse(User.objects.filter(username='testuser').exists())

class RegisterFormTestCase(TestCase):
    def test_valid_form(self):
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'rut': '12345678',
            'password': 'testpassword',
        }
        form = Registerform(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {
            'username': 'testuser',
            'email': 'invalid_email',  # Provoca un error de validación
            'rut': '12345678',
            'password': 'testpassword',
        }
        form = Registerform(data=form_data)
        self.assertFalse(form.is_valid())
