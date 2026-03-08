import pandas as pd
import sqlite3

# Extract
df = pd.read_csv("data/sales.csv")

# Load to database
conn = sqlite3.connect("database/sales.db")

df.to_sql("sales", conn, if_exists="replace", index=False)

print("ETL process completed")
