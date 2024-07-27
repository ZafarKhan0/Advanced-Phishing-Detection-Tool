import unittest
from src.model_training import train_model
from src.data_collection import load_data, preprocess_data
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from model_training import train_model

class TestModelTraining(unittest.TestCase):
    def setUp(self):
        phishing_path = 'D:\\ZafarKhanProjects\\Advanced-Phishing-Detection-Tool\\data\\phishing.csv'
        legitimate_path = 'D:\\ZafarKhanProjects\\Advanced-Phishing-Detection-Tool\\data\\legitimate.csv'
        data = load_data(phishing_path, legitimate_path)
        self.X_train, self.X_test, self.y_train, self.y_test = preprocess_data(data)

    def test_train_model(self):
        model = train_model(self.X_train, self.y_train)
        self.assertIsNotNone(model)
    
    pass
  
if __name__ == '__main__':
    unittest.main()
