from flask import Flask, render_template, request
import numpy as np
import joblib
import os

app = Flask(__name__)

# Train model on startup if model.pkl doesn't exist
if not os.path.exists('model.pkl'):
    import train

model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html', prediction=None, version="1.0")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        study_hours = float(request.form['study_hours'])
        attendance = float(request.form['attendance'])
        internal_marks = float(request.form['internal_marks'])
        
        features = np.array([[study_hours, attendance, internal_marks]])
        prediction = model.predict(features)[0]
        result = "Pass 🎉" if prediction == 1 else "Fail ❌"
        
        return render_template('index.html', prediction=result, version="1.0")
    except Exception as e:
        return render_template('index.html', prediction=f"Error: {str(e)}", version="1.0")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
from flask import Flask, render_template

app = Flask(__name__, template_folder='.')
