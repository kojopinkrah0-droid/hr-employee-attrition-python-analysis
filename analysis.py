import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

DATA = Path("data/hr_attrition_cleaned.csv")
OUT = Path("assets")
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA)
if "AttritionFlag" not in df:
    df["AttritionFlag"] = (df["Attrition"] == "Yes").astype(int)

print("Shape:", df.shape)
print("Missing values:", int(df.isna().sum().sum()))
print("Attrition rate:", f"{df['AttritionFlag'].mean():.2%}")

for col in ["Department", "JobRole", "OverTime", "BusinessTravel", "MaritalStatus"]:
    summary = (df.groupby(col)
                 .agg(Employees=("EmployeeNumber","count"),
                      Attritions=("AttritionFlag","sum"),
                      AttritionRate=("AttritionFlag","mean"))
                 .sort_values("AttritionRate", ascending=False))
    print(f"\n{col}\n", summary)

numeric = df.select_dtypes(include=np.number)
print("\nCorrelation with attrition:\n",
      numeric.corr(numeric_only=True)["AttritionFlag"]
             .drop("AttritionFlag")
             .sort_values())
