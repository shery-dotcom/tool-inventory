import pandas as pd
from slugify import slugify

# Load raw data
df = pd.read_csv("data/sample.csv")

# Clean data
df["name"] = df["name"].str.strip()
df["description"] = df["description"].str.strip()
df["slug"] = df["name"].apply(slugify)
df = df.drop_duplicates(subset=["slug"])
df["pricing"] = df["pricing"].str.strip()

# Save processed file
df.to_csv("data/processed/processed_data.csv", index=False)
print("Data cleaned and saved to data/processed/processed_data.csv")
