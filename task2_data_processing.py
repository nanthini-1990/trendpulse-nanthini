# task2_data_processing.py

# Import required library
import pandas as pd

# Step 1: Load JSON file
# Replace the file name with your actual date if needed
file_path = "data/trends_20260408.json"

try:
    df = pd.read_json(file_path)
    print(f"Loaded {len(df)} stories from {file_path}")
except Exception as e:
    print("Error loading JSON file:", e)
    exit()

# Step 2: Clean the Data

# 1. Remove duplicate stories based on post_id
df = df.drop_duplicates(subset="post_id")
print("After removing duplicates:", len(df))

# 2. Remove rows with missing important values
df = df.dropna(subset=["post_id", "title", "score"])
print("After removing nulls:", len(df))

# 3. Convert data types (ensure numeric values)
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)

# 4. Remove low-quality stories (score < 5)
df = df[df["score"] >= 5]
print("After removing low scores:", len(df))

# 5. Remove extra whitespace from titles
df["title"] = df["title"].str.strip()

# Step 3: Save cleaned data as CSV

output_path = "data/trends_clean.csv"

df.to_csv(output_path, index=False)

print(f"\nSaved {len(df)} rows to {output_path}")

# Step 4: Print summary (stories per category)
print("\nStories per category:")
print(df["category"].value_counts())