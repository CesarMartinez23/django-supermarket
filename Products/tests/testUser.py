from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

# Create your tests here.


class createUsers(TestCase):
    def test_createUser(self):
        User.objects.create_user(username='test', password='test1234567890')


class validatePassword(TestCase):
    def test_validatePassword(self):
        validate_password('test1234567890')
