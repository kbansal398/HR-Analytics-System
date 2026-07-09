import pandas as pd

# Load the HR Analytics dataset
df = pd.read_csv("data/raw/employee_data.csv")

print("=" * 60)
print("HR ANALYTICS - EXPLORATORY DATA ANALYSIS")
print("=" * 60)

# Total number of employees
total_employees = len(df)
print("\nTotal Employees:", total_employees)

# Total number of departments
total_departments = df["Department"].nunique()
print("\nTotal Departments:", total_departments)

# Department names
print("\nDepartment Names:")
print(df["Department"].unique())

# Total number of job roles
total_job_roles = df["JobRole"].nunique()
print("\nTotal Job Roles:", total_job_roles)

# Job role names
print("\nJob Role Names:")
print(df["JobRole"].unique())

# Total employees who left the company
attrition_count = df[df["Attrition"] == "Yes"].shape[0]

# Attrition Rate
attrition_rate = (attrition_count / len(df)) * 100

print("\nTotal Employees Left:", attrition_count)
print("Attrition Rate: {:.2f}%".format(attrition_rate))