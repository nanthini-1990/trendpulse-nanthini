import pandas as pd

try:
    print("Loading raw data...")

    # Load data
    df = pd.read_csv("raw_data.csv")

    # Show initial data
    print("Original Data:")
    print(df.head())

    # 🔹 Clean column names (remove spaces if any)
    df.columns = df.columns.str.strip()

    # 🔹 Handle missing values
    df = df.dropna()

    # 🔹 Convert date column (if exists)
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

    if "time" in df.columns:
        df["time"] = pd.to_datetime(df["time"], errors="coerce")

    # 🔹 Save cleaned data
    df.to_csv("cleaned_data.csv", index=False)

    print("✅ Data cleaned successfully and saved as cleaned_data.csv")

except FileNotFoundError:
    print("❌ raw_data.csv not found. Run Task 1 first.")

except Exception as e:
    print("❌ Error occurred:", e)