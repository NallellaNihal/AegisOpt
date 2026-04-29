import sqlite3
import pandas as pd
from sklearn.linear_model import LogisticRegression
import numpy as np

DB_PATH = "data/metrics.db"

class MLModel:
    def load_data(self):
        conn = sqlite3.connect(DB_PATH)
        df = pd.read_sql_query("SELECT * FROM runs", conn)
        conn.close()
        return df

    def train(self):
        df = self.load_data()

        if len(df) < 5:
            return None  # Not enough data

        # Features
        X = df[["functions", "loops"]]

        # Label: optimize if execution_time > threshold
        y = (df["execution_time"] > df["execution_time"].mean()).astype(int)

        model = LogisticRegression()
        model.fit(X, y)

        return model

    def predict(self, model, profile):
        if model is None:
            return "Not enough data for ML decision"

        features = np.array([[profile["functions"], profile["loops"]]])
        pred = model.predict(features)[0]

        return "Optimize" if pred == 1 else "No optimization needed"