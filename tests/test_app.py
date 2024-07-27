import unittest
import json
from src.app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_prediction(self):
        # Example feature vector; replace with actual test data if available
        features = [0.1, 0.2, 0.3, 0.4, 0.5]
        response = self.app.post('/predict', json={'features': features})
        self.assertEqual(response.status_code, 200)
        self.assertIn('prediction', response.get_json())

if __name__ == '__main__':
    unittest.main()
