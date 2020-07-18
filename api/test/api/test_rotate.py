import os
import unittest
import requests

from src import FLASK_PORT
from src.helper import image_utils


class APIRotateTest(unittest.TestCase):

    def setUp(self):
        self.endpoint = f'http://localhost:{FLASK_PORT}/rotate'
        self.image_base64 = image_utils.encode(os.path.join('..', 'docs', 'images', 'example_1_input.png'))

    def test_success(self):
        request_body = dict(image_base64=self.image_base64)
        response = requests.post(self.endpoint, json=request_body).json()
        self.assertIn('error', response)
        self.assertIn('response', response)
        self.assertNotIn('message', response)
        self.assertIn('image_base64', response['response'])
        self.assertFalse(response['error'])
