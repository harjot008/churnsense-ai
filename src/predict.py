from pathlib import Path
import joblib
import pandas as pd


# Project root folder
ROOT_DIR = Path(__file__).resolve().parent.parent

# Exact saved model path
PIPELINE_PATH = ROOT_DIR / "models" / "churn_pipeline.joblib"

# Load the fitted pipeline
pipeline = joblib.load(PIPELINE_PATH)

def predict_customer(customer_df: pd.DataFrame):
    prediction = pipeline.predict(customer_df)[0]

    return int(prediction) # Cause we want normal int instead of numpy int
