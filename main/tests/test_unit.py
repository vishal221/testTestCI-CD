import unittest
import requests
import pytest
import requests_mock

from flask import url_for
from flask_testing import TestCase

from app import app

from application.routes import index, date

class TestInit(TestCase):
    def create_app(self):
        config_name = 'testing'
        app.config.update(
            WTF_CSRF_ENABLED=False,
            DEBUG=True
            )
        return app

    def setUp(self):
        print("-----------")

    def tearDown(self):
        print("--------")

class TestMain(TestInit):
    
    def test_converter(self):
        with requests_mock.mock() as m:
            m.post('http://converter:5001/date/1986')

            response = self.client.get(
                ('http://main:5000/')
            )
            self.assertIn(b'Birth Year:', response.data)

    def test_prime(self):
        with requests_mock.mock() as m:
            m.post('http://prime:5002/date/1986')

            response = self.client.get(
                ('http://main:5000/')
            )
            self.assertIn(b'Birth Year:', response.data)

    
    def test_converter(self):
        
        with requests_mock.mock() as m:
            m.post('http://converter:5001/result/10')

            response = self.client.get(
                ('http://main:5000/')
            )
            self.assertIn(b'Amount:', response.data)

            # random comment here

    
    
    
