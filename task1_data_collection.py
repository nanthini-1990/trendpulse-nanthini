import requests
import pandas as pd

API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

try:
    print("Fetching data...")

    response = requests.get(API_URL, timeout=10)

    if response.status_code == 200:
        data = response.json()

        record = {
            "base": data["base"],
            "date": data["date"],
            "INR_rate": data["rates"]["INR"],
            "EUR_rate": data["rates"]["EUR"],
            "GBP_rate": data["rates"]["GBP"]
        }

        df = pd.DataFrame([record])
        df.to_csv("raw_data.csv", index=False)

        print("✅ Data collected successfully")

    else:
        print("❌ Failed:", response.status_code)

except Exception as e:
    print("❌ Error:", e)