import pandas as pd
from config import RAW_DATA_PATH

# Load Dataset
df = pd.read_csv(RAW_DATA_PATH)

print("=" * 60)
print("HR ANALYTICS DATASET")
print("=" * 60)

print("\nFirst 5 Rows")
print(df.head())

print("\nDataset Shape")
print(df.shape)

print("\nColumns")
print(df.columns.tolist())

print("\nData Types")
print(df.dtypes)

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())