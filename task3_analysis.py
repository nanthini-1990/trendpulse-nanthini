import pandas as pd

try:
    print("Loading cleaned data...")

    df = pd.read_csv("cleaned_data.csv")

    print("\nDataset Preview:")
    print(df.head())

    print("\n🔍 Basic Analysis:")

    # Select only numeric columns
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

    print("\nNumeric Columns:", list(numeric_cols))

    for col in numeric_cols:
        print(f"\nAnalysis for {col}:")
        print("Mean:", df[col].mean())
        print("Max:", df[col].max())
        print("Min:", df[col].min())

    print("\n✅ Analysis completed successfully")

except FileNotFoundError:
    print("❌ cleaned_data.csv not found. Run Task 2 first.")

except Exception as e:
    print("❌ Error occurred:", e)