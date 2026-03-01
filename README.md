# 🧾 Car Price Predictor – ML Deployment with Flask

_Predicting used car prices based on brand, age, and kilometers driven using a pre-trained ML model deployed as a web app._

---

## 📌 Table of Contents
- <a href="#overview">Overview</a>
- <a href="#business-problem">Project Goal</a>
- <a href="#dataset">Dataset</a>
- <a href="#tools--technologies">Tools & Technologies</a>
- <a href="#project-structure">Project Structure</a>
- <a href="#data-cleaning--preparation">Data Preparation</a>
- <a href="#exploratory-data-analysis-eda">Model Training & Analysis</a>
- <a href="#research-questions--key-findings">Key Features & Insights</a>
- <a href="#dashboard">Web Interface</a>
- <a href="#how-to-run-this-project">How to Run This Project</a>
- <a href="#final-recommendations">Future Improvements</a>
- <a href="#author--contact">Author & Contact</a>

---
<h2><a class="anchor" id="overview"></a>Overview</h2>

This project is a simple web application that predicts the resale price of used cars using a pre-trained machine learning model. Users can input the car brand (Mahindra, Maruti, or Tata), age in years, and kilometers driven to get an estimated price. The app is built with Flask for the backend and HTML/CSS for the frontend, serving as a beginner's demonstration of ML model deployment.

---
<h2><a class="anchor" id="business-problem"></a>Project Goal</h2>

Estimating used car prices accurately helps buyers, sellers, and dealerships make informed decisions. This project aims to:
- Deploy a basic ML model as an interactive web app
- Handle user inputs and provide real-time predictions
- Demonstrate end-to-end ML workflow from model loading to user interface
- Focus on simplicity for educational purposes as a first ML project

---
<h2><a class="anchor" id="dataset"></a>Dataset</h2>

- Assumed training data: CSV or similar with columns like `age_years`, `kms_driven`, and car brands (one-hot encoded as Mahindra, Maruti, Tata)
- Pre-trained model and scaler saved as pickle files (`cp.pkl` and `scaler.pkl`)
- No raw data included; model assumes regression on historical car sales data

---

<h2><a class="anchor" id="tools--technologies"></a>Tools & Technologies</h2>

- Python (Flask for web framework, Scikit-learn for ML model)
- HTML/CSS (with Google Fonts for styling)
- Pickle (for model serialization)
- GitHub

---
<h2><a class="anchor" id="project-structure"></a>Project Structure</h2>
car-price-predictor/
│
├── README.md
├── .gitignore
├── app.py              # Main Flask application script
├── cp.pkl              # Pre-trained ML model
├── scaler.pkl          # Feature scaler
│
├── templates/          # Folder for HTML templates
│   └── home.html       # UI template for the web form
text---
<h2><a class="anchor" id="data-cleaning--preparation"></a>Data Preparation</h2>

- User inputs: Brand (as integer), age (float), kms driven (float)
- One-hot encoding for brands to match training order: ['age_years', 'kms_driven', 'car_name_Mahindra', 'car_name_Maruti', 'car_name_Tata']
- Scaling inputs using loaded scaler
- Prediction ensures non-negative prices (floored at 0)

---
<h2><a class="anchor" id="exploratory-data-analysis-eda"></a>Model Training & Analysis</h2>

**Assumptions from Training:**
- Model: Regression (e.g., Linear Regression or similar from Scikit-learn)
- Features: Age, kms, and brand dummies
- No explicit EDA in this deployment; assume prior analysis showed:
  - Negative correlation between age/kms and price
  - Brand-specific pricing variations

**Potential Issues:**
- Negative predictions handled by max(0, price)
- Outliers in inputs not validated (e.g., negative age)

---
<h2><a class="anchor" id="research-questions--key-findings"></a>Key Features & Insights</h2>

1. **Supported Brands**: Limited to Mahindra, Maruti, Tata for simplicity
2. **Prediction Logic**: Real-time scaling and inference
3. **User Experience**: Simple form with instant results in thousands (e.g., "Expected Price = 150.25 K")
4. **Insights**: Older cars or high kms reduce price; brands impact baseline value
5. **Limitations**: No advanced features like multiple models or error handling

---
<h2><a class="anchor" id="dashboard"></a>Web Interface</h2>

- Flask-based web app shows:
  - Dropdown for brand selection
  - Inputs for age and kms
  - Predicted price display
  - Modern styling with Poppins font


---
<h2><a class="anchor" id="how-to-run-this-project"></a>How to Run This Project</h2>

1. Clone the repository:
git clone https://github.com/yourusername/car-price-predictor.git

Install dependencies:

Bashpip install flask

Run the app:

Bashpython app.py

Open in browser:
Visit http://localhost:5000
Enter details and predict!


<h2><a class="anchor" id="final-recommendations"></a>Future Improvements</h2>

1. Add more car brands and features (e.g., fuel type)
2. Implement input validation and error messages
3. Deploy to cloud (e.g., Heroku)
4. Include training notebook for full reproducibility
5. Enhance with JavaScript for dynamic UI

<h2><a class="anchor" id="author--contact"></a>Author & Contact</h2>

Name: Namrata Pokharkar
📧 Email: namratapokharkar20@gmail.com
🔗 LinkedIn: www.linkedin.com/in/namrata-pokharkar-862a55288
