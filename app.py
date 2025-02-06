from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load("model/house_price_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from form
        MedInc = float(request.form['MedInc'])
        HouseAge = float(request.form['HouseAge'])
        AveRooms = float(request.form['AveRooms'])
        AveOccup = float(request.form['AveOccup'])

        # Make prediction
        features = np.array([[MedInc, HouseAge, AveRooms, AveOccup]])
        prediction = model.predict(features)[0]

        return render_template('index.html', prediction_text=f'Estimated House Price: ${prediction:,.2f}')

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)
