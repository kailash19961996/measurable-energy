from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)
model = joblib.load('anomaly_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Expect JSON input like {"power": 1.5} (in kilowatts)
    data = request.get_json()
    power = float(data['power'])
    
    # Predict (1 = normal, -1 = anomaly)
    prediction = model.predict([[power]])[0]
    result = "Anomaly" if prediction == -1 else "Normal"
    
    return jsonify({"power": power, "result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)