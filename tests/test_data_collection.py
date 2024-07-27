import unittest
import os
from src.data_collection import load_data

class TestDataCollection(unittest.TestCase):
    def setUp(self):
        phishing_path = 'D:\\ZafarKhanProjects\\Advanced-Phishing-Detection-Tool\\data\\phishing.csv'  
        legitimate_path = 'D:\\ZafarKhanProjects\\Advanced-Phishing-Detection-Tool\\data\\legitimate.csv'  
        self.data = load_data(phishing_path, legitimate_path)

    def test_load_data(self):
        self.assertIsNotNone(self.data)

if __name__ == '__main__':
    unittest.main()
