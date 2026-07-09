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



print("\nUnique Departments:")
print(df["Department"].unique())

print("\nUnique Job Roles:")
print(df["JobRole"].unique())

print("\nUnique Attrition Values:")
print(df["Attrition"].unique())

print("\nSummary Statistics:")
print(df.describe())