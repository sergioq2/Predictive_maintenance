import unittest
from fastapi.testclient import TestClient
import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_predict_endpoint(self):
        data = {
            "Type": "M",
            "Air_temperature": 298.1,
            "Process_temperature": 308.6,
            "Rotational_speed": 1551,
            "Torque": 42.8,
            "Tool_wear": 5.0,
        }

        response = self.client.post("/predict", json=data)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIn("prediction", result)
        self.assertIsInstance(result["prediction"], float)

def test_suite():
    test_loader = unittest.TestLoader()
    test_runner = unittest.TextTestRunner()
    test_result = test_runner.run(test_loader.loadTestsFromModule(app))

if __name__ == "__main__":
    test_suite()     