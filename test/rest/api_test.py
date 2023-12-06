import http.client
import os
import unittest
# Añadir import de Request 
from urllib.request import Request, urlopen
import pytest

BASE_URL = "http://192.168.64.10:5000"
BASE_URL_MOCK = "http://192.168.64.10:9090"
DEFAULT_TIMEOUT = 10  # in secs

@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/1/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            response.read().decode(), "3", "ERROR ADD"
        )

    def test_api_sqrt(self):
        
        #response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        resp = Request(
            url = f"{BASE_URL_MOCK}/calc/sqrt/64",
            headers={'User-Agent': 'Mozilla/5.0'}            
        )
        response = urlopen(resp).read()
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            response.read().decode(), "8", "ERROR SQRT"
        )

if __name__ == "__main__":  # pragma: no cover
    unittest.main()
