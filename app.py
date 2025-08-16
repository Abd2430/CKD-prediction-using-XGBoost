from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load model and feature list
model = joblib.load('xgb_model_reduced.pkl')
features = joblib.load('features.pkl')  # Should match the list above exactly

@app.route('/')
def home():
    return render_template('index.html', features=features)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = {feature: float(request.form[feature]) for feature in features}
        input_df = pd.DataFrame([input_data], columns=features)
        prediction = model.predict(input_df)[0]
        result = "CKD Detected" if prediction == 1 else "No CKD"
        return render_template('index.html', prediction=result, features=features)
    except KeyError as e:
        return f"Missing input for: {e}", 400

if __name__ == '__main__':
    print("Starting CKD app...")
    app.run(debug=True)
