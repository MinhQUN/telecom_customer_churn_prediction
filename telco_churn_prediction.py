import pandas as pd
import numpy as np

df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
print(f"DataShape: {df.shape}")
print(df.info())
print(df.head())