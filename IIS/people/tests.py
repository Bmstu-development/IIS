from django.test import TestCase, Client
from django.contrib.auth import get_user_model

from .models import Person

User = get_user_model()


class TestURL(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        global p
        p = Person.objects.create(
            surname='Тестович',
            name='Тест',
            organisation='Тестирование'
        )

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        p.delete()

    def setUp(self):
        self.guest = Client()
        self.user = User.objects.create_user(username='test')
        self.auth_user = Client()
        self.auth_user.force_login(self.user)

    def tearDown(self):
        self.user.delete()

    def test_auth(self):
        response = self.guest.get('/')
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/accounts/login/?next=/')
        response = self.auth_user.get('/')
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/people/')

        response = self.guest.get('/people/')
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/accounts/login/?next=/people/')
        response = self.auth_user.get('/people/')
        self.assertEquals(response.status_code, 200)

        # response = self.guest.get('/people/add')
        # self.assertEquals(response.status_code, 302)
        # self.assertEquals(response.url, '/accounts/login/?next=/people/add')
        # response = self.auth_user.get('/people/add')
        # self.assertEquals(response.status_code, 200)

        response = self.guest.get(f'/people/{p.id}')
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, f'/accounts/login/?next=/people/{p.id}')
        response = self.auth_user.get(f'/people/{p.id}')
        self.assertEquals(response.status_code, 200)

        response = self.guest.get(f'/people/{p.id + 1}')
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, f'/accounts/login/?next=/people/{p.id + 1}')
        response = self.auth_user.get(f'/people/{p.id + 1}')
        self.assertEquals(response.status_code, 404)
