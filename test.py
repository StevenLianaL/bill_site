from unittest import TestCase

from starlette.testclient import TestClient

from app.main import app


class TestApi(TestCase):
    def setUp(self) -> None:
        self.c = TestClient(app)

    def test_get_all(self):
        response = self.c.get('/bill/all')
        self.assertEqual(response.status_code, 200)
