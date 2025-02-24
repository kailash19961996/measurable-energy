# Energy Anomaly Detector
A simple ML pipeline to detect anomalies in energy consumption data.

## How to Run
1. Preprocess: `python preprocess.py`
2. Train: `python train_model.py`
3. Run locally: `python app.py`
4. Or use Docker: `docker build -t energy-anomaly-detector . && docker run -p 5000:5000 energy-anomaly-detector`
5. Test: `curl -X POST -H "Content-Type: application/json" -d '{"power": 1.5}' http://localhost:5000/predict`