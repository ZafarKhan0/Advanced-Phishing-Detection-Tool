# Machine Learning
## Overview
The Advanced Phishing Detection Tool is a machine learning-based application designed to identify phishing attempts with high accuracy. Utilizing state-of-the-art machine learning algorithms, this tool analyzes email and website features to detect potential phishing attacks.

## Features
Real-Time Phishing Detection: Predicts whether a given URL or email is a phishing attempt.
Machine Learning Model: Trained using a robust dataset to achieve high accuracy in phishing detection.
API Interface: Provides an easy-to-use API for integration with other applications.

## Installation
-Clone the repository:
  git clone https://github.com/ZafarKhan0/Advanced-Phishing-Detection-Tool-Using-MachineLearning.git
  cd Advanced-Phishing-Detection-Tool-Using-MachineLearning


-Create a virtual environment and activate it:
  python -m venv venv
  source venv/bin/activate  # On Windows use venv\Scripts\activate


-Install the required packages:
  pip install -r requirements.txt


## Usage
## Running the Application
 
-Start the Flask server:
  python src/app.py

-Access the API:

 Home Endpoint:
  GET http://127.0.0.1:5000/
  

 Predict Endpoint:
  POST http://127.0.0.1:5000/predict

Request body example:
{
  "features": [0.1, 0.2, 0.3, 0.4, 0.5]
}
Returns the prediction result.


## Running Tests
To run the unit tests:
python -m unittest discover -s tests

## Data
The project uses sample datasets for training and testing. Ensure you have phishing.csv and legitimate.csv in the data/ directory.

## Contributing
Feel free to contribute to this project by submitting pull requests or opening issues. Your contributions are greatly appreciated!

## Contact
For any questions or further information, you can reach me at K213567@NU.EDU.PK

