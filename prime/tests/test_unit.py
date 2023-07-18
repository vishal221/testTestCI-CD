import unittest
import requests
import pytest
import requests_mock

from flask import url_for
from flask_testing import TestCase

from app import app

from application.routes import prime 


class TestBase(TestCase):
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


class TestPrime(unittest.TestCase):

    def test_values(self):
        
        self.assertEqual(prime(1989), 'composite', msg='Equal')
        self.assertEqual(prime(1988), 'composite', msg='Equal')
        self.assertEqual(prime(1986), 'composite', msg='Equal')
        self.assertEqual(prime(1987), 'prime', msg='Equal')
        self.assertEqual(prime(1985), 'composite', msg='Equal')
        self.assertEqual(prime(1984), 'composite', msg='Equal')
        self.assertEqual(prime(1983), 'composite', msg='Equal')
        self.assertEqual(prime(1982), 'composite', msg='Equal')
        self.assertEqual(prime(1981), 'composite', msg='Equal')
        self.assertEqual(prime(2), 'prime', msg='Equal')
        self.assertEqual(prime(1), 'neither prime nor composite', msg='Equal')
        self.assertEqual(prime(0), 'You do not appear to exist', msg='Equal')
        self.assertEqual(prime(-1986), 'You do not appear to exist', msg='Equal')
 