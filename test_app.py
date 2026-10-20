import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_content(self):
        response = self.client.get("/")
        self.assertEqual(response.data.decode("utf-8"), "Hola Docker")

if __name__ == "__main__":
    unittest.main()
