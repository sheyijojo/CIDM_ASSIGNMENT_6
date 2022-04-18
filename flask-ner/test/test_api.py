import unittest
import json
from flask import request

from app import app

class TestApi(unittest.TestCase):

    def test_ner_endpoint_given_json_body_returns_200(self):
        with app.test_client() as client:
            response = client.post('/ner', json={"sentence": "Sheyi is getting the test driven approach right. "})
            assert response._status_code == 200
