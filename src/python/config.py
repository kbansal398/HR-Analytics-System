import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))

RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "employee_data.csv")

PROCESSED_DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "employee_cleaned.csv")