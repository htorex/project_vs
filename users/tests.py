from django.test import TestCase

from .models import User
from vs.forms import Registerform

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

    def test_existing_username(self):
        User.objects.create_user(username='testuser', password='testpassword')

        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'rut': '12345678',
            'password': 'testpassword',
        }
        form = Registerform(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('el username ya se encuentra registrado', form.errors['username'])

    def test_existing_email(self):
        User.objects.create_user(username='existinguser', email='test@example.com', password='testpassword')

        form_data = {
            'username': 'testuser',
            'email': 'test@example.com', 
            'rut': '12345678',
            'password': 'testpassword',
        }
        form = Registerform(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('el email ya se encuentra registrado', form.errors['email'])

    def test_existing_rut(self):
        User.objects.create_user(username='existinguser2', rut='12345678', password='testpassword')

        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'rut': '12345678',  
            'password': 'testpassword',
        }
        form = Registerform(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('el rut ya se encuentra registrado', form.errors['rut'])
