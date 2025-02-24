import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# Load preprocessed data
df = pd.read_csv('energy_data.csv', index_col='datetime', parse_dates=True)
data = df.values.reshape(-1, 1)  # Reshape for sklearn

# Train Isolation Forest
model = IsolationForest(contamination=0.05, random_state=42)  # 5% anomalies
model.fit(data)

# Save the model
joblib.dump(model, 'anomaly_model.pkl')
print("Model trained and saved as anomaly_model.pkl")