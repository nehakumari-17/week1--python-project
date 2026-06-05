import pandas as pd
import os
# Load CSV file
file_path = os.path.join(os.path.dirname(__file__), "sales_data (1).csv")
df = pd.read_csv(file_path)

print("\nFIRST 5 ROWS")
print(df.head())

print("\nDATA INFORMATION")
print(df.info())

print("\nTOTAL SALES")
print(df["Total_Sales"].sum())

print("\nAVERAGE SALES")
print(df["Total_Sales"].mean())

print("\nMAXIMUM SALE")
print(df["Total_Sales"].max())

print("\nMINIMUM SALE")
print(df["Total_Sales"].min())