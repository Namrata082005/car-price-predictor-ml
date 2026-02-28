from flask import *
from pickle import load

# Load model
with open("cp.pkl", "rb") as f:
    model = load(f)

# Load scaler
with open("scaler.pkl", "rb") as f:
    scaler = load(f)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        car_choice = int(request.form.get("car_choice"))
        yrs = float(request.form.get("yrs"))
        kms = float(request.form.get("kms"))

        # Match training dummy variable order:
        # ['age_years', 'kms_driven', 'car_name_Mahindra', 'car_name_Maruti', 'car_name_Tata']
        if car_choice == 1:
            d = [[yrs, kms, 1, 0, 0]]
        elif car_choice == 2:
            d = [[yrs, kms, 0, 1, 0]]
        else:
            d = [[yrs, kms, 0, 0, 1]]

        # Scale input data
        row_scaled = scaler.transform(d)

        # Predict price
        price = model.predict(row_scaled)[0]
        price = max(price, 0)  # Avoid negative prices

        msg = f"Expected Price = {round(price, 2)} K"
        return render_template("home.html", msg=msg)
    else:
        return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
