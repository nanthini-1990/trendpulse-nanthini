import pandas as pd
import matplotlib.pyplot as plt

try:
    print("Loading cleaned data...")

    df = pd.read_csv("cleaned_data.csv")

    print("Creating visualization...")

    # Select only numeric columns
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

    for col in numeric_cols:
        plt.plot(df[col], marker='o', label=col)

    plt.title("TrendPulse Data Visualization")
    plt.xlabel("Index")
    plt.ylabel("Values")
    plt.legend()
    plt.grid()

    # Save image
    plt.savefig("trend.png")

    # Show graph
    plt.show()

    print("✅ Visualization created successfully")

except FileNotFoundError:
    print("❌ cleaned_data.csv not found. Run Task 2 first.")

except Exception as e:
    print("❌ Error occurred:", e)