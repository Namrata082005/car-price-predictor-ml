Car Price Predictor

<img width="1816" height="851" alt="image" src="https://github.com/user-attachments/assets/e4e3b00d-e10b-4c46-91c1-d31b61a95c72" />

Overview:

This is a simple web application built with Flask that predicts the price of used cars based on their brand, age (in years), and kilometers driven. It uses a pre-trained machine learning model to estimate the expected resale price. The supported car brands are Mahindra, Maruti, and Tata. This project serves as a beginner-friendly demonstration of deploying an ML model as a web app.
The app features a clean, user-friendly interface where users can input details and get instant predictions. It's my first ML project, showcasing end-to-end development from model training (assumed) to deployment.



Features Interactive Form: Select car brand from a dropdown, enter age and kms driven.
Real-Time Predictions: Displays the predicted price in thousands (e.g., "Expected Price = 150.25 K").
Data Handling: Uses one-hot encoding for brands and scaling for numerical features.
Error Prevention: Ensures predicted prices are non-negative.
Responsive Design: Modern styling with Poppins font and subtle CSS for a professional look.
Debug Mode: Runs in debug mode for easy development and testing.



Technologies Used:

Backend: Python 3 with Flask (web framework)
Machine Learning: Scikit-learn (for the regression model and scaler, loaded via pickle)
Frontend: HTML5, CSS3 (with Google Fonts)
Dependencies: Flask, pickle (built-in)
Model Files: cp.pkl (pre-trained model), scaler.pkl (feature scaler)



How It Works: 

1. Model Loading: On startup, the app loads the pre-trained model and scaler from pickle files.
2. User Input: Via a POST form, users provide car brand (as an integer: 1=Mahindra, 2=Maruti, 3=Tata), age in years, and kms driven.
3. Data Preparation: Creates a feature array with age, kms, and one-hot encoded brand dummies (order: Mahindra, Maruti, Tata).
Scales the input using the loaded scaler.
4. Prediction: The model predicts the price, which is rounded and displayed (floored at 0 if negative).
5. Output: Renders the result on the same page using Jinja templating.
6. The ML model is assumed to be a regressor trained on a dataset with features like age_years, kms_driven, and brand dummies.


Installation and Setup
Prerequisites
1. Python 3.6+ installed
2. Git (for cloning the repo)



Steps:

1. Clone the Repository:textgit clone https://github.com/yourusername/car-price-predictor.git
cd car-price-predictor
2. Install Dependencies:textpip install flask
3. Ensure Files are Present:
  app.py: Main Flask application.
  templates/home.html: HTML template for the UI.
  cp.pkl: Pickled ML model.
  scaler.pkl: Pickled scaler.


Run the Application:textpython app.py
The app will start on http://127.0.0.1:5000 (or http://localhost:5000).
Open this URL in your browser to use the predictor.


Testing:

Example Input: Brand = Mahindra, Age = 2.5 years, Kms = 15000.
Expected: A prediction like "Expected Price = X.XX K".
Stop the server with Ctrl+C in the terminal.

'''
Project Structure:
textcar-price-predictor/
├── app.py           # Main Flask app script
├── cp.pkl           # Pre-trained ML model
├── scaler.pkl       # Feature scaler
├── templates/       # Folder for HTML templates
│   └── home.html    # UI template
└── README.md        # This file
'''


Limitations:

1. Supports only three car brands; predictions may not generalize to others.
2. No robust error handling for invalid inputs (e.g., non-numeric values crash the app).
3. Assumes the model was trained on specific feature order—mismatches could lead to inaccurate predictions.
4. Local-only deployment; not optimized for production (e.g., debug mode enabled).
5. No data validation for realistic ranges (e.g., negative age/kms allowed but not ideal).


Future Improvements:

1. Add more brands and features (e.g., fuel type, transmission).
2. Implement input validation and error messages.
3. Deploy to a cloud platform like Heroku or Vercel for public access.
4. Integrate a database for logging predictions or user feedback.
5. Enhance UI with JavaScript for real-time validation or charts.
6. Retrain the model with a larger dataset for better accuracy.

Author & Contact:

Name: Namrata Pokharkar

Contact: 9356455954

email: namratapokharkar20@gmail.com
