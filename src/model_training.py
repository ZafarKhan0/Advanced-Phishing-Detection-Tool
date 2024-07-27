import os
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from data_collection import load_data, preprocess_data

def train_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

if __name__ == "__main__":
    current_dir = os.path.dirname(__file__)
    phishing_file = os.path.join(current_dir, '../data/phishing.csv')
    legitimate_file = os.path.join(current_dir, '../data/legitimate.csv')

    data = load_data(phishing_file, legitimate_file)
    X_train, X_test, y_train, y_test = preprocess_data(data)
    
    model = train_model(X_train, y_train)
    
    # Ensure the models directory exists
    model_dir = os.path.join(current_dir, '../models')
    os.makedirs(model_dir, exist_ok=True)

    # Save the model
    model_path = os.path.join(model_dir, 'phishing_model.pkl')
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)

    # Evaluate the model
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred)
    print(report)
