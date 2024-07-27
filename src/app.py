import pickle
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Define the path to the model file
model_path = os.path.join(os.path.dirname(__file__), '../models/phishing_model.pkl')

def load_model(model_file):
    with open(model_file, 'rb') as f:
        return pickle.load(f)

# Load the model
model = load_model(model_path)

@app.route('/')
def home():
    return "Welcome to the Phishing Detection API. Use the /predict endpoint to make predictions."

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)  # Force JSON parsing
        print(data)  # Log received data for debugging
        features = [data['features']]
        prediction = model.predict(features)
        return jsonify({'prediction': int(prediction[0])})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
