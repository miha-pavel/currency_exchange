# coding=utf-8
import json

from django.test import TestCase
from django.urls import reverse
from django.test.client import Client

from faker import Faker

from .models import User


fake = Faker()


class BaseTest(TestCase):
    """ Base class for the shop tests

    """

    @classmethod
    def setUpClass(cls):
        super(BaseTest, cls).setUpClass()
        cls.client = Client()
        cls.username = 'admin'
        cls.email = 'admin@admin.com'
        cls.password = '1234567'
        cls.admin = User.objects.create(
            username=cls.username,
            email=cls.email,
            first_name=fake.first_name(),
            last_name=fake.last_name(),
        )
        cls.admin.set_password(cls.password)
        cls.admin.save()


class TestTemplateView(TestCase):
    """
    """

    def test_visit_home_page(self):
        """ 1. Check render home page
        """
        url = reverse('home')
        response = self.client.get(url)
        expected_status = 200
        self.assertEqual(response.status_code, expected_status)
        self.assertTrue(len(response.context))
        self.assertTemplateUsed(response, 'home.html')


class TestAcountView(BaseTest):

    def test_login(self):
        url = reverse('login')
        response = self.client.get(url,
        kwargs={'username': self.username, 'password': self.username})
        print('response: ', response)
        expected_status = 200
        self.assertEqual(response.status_code, expected_status)
    
    def test_logout(self):
        self.client.login(username=self.username, password=self.password)
        url = reverse('logout')
        response = self.client.get(url)
        expected_status = 302
        self.assertEqual(response.status_code, expected_status)
        self.assertRedirects(response, '/')

