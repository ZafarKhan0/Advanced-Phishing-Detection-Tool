import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def load_data(phishing_file, legitimate_file):
    phishing_data = pd.read_csv(phishing_file)
    legitimate_data = pd.read_csv(legitimate_file)
    phishing_data['label'] = 1
    legitimate_data['label'] = 0
    data = pd.concat([phishing_data, legitimate_data], ignore_index=True)
    return data

def preprocess_data(data):
    # Select relevant numeric features; if any feature contains text, handle it appropriately
    feature_columns = [
        'NumDots', 'SubdomainLevel', 'PathLevel', 'UrlLength', 'NumDash', 
        # Add all other relevant numeric columns
    ]
    
    if 'label' not in data.columns:
        raise KeyError("The expected column 'label' was not found in the dataset.")
    
    X = data[feature_columns]
    y = data['label']
    
    # Handle any categorical features if present
    for column in X.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        X[column] = le.fit_transform(X[column])
    
    # Ensure all data is numeric and handle missing values
    X = X.apply(pd.to_numeric, errors='coerce').fillna(0)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    current_dir = os.path.dirname(__file__)
    phishing_file = os.path.join(current_dir, '../data/phishing.csv')
    legitimate_file = os.path.join(current_dir, '../data/legitimate.csv')

    data = load_data(phishing_file, legitimate_file)
    X_train, X_test, y_train, y_test = preprocess_data(data)
