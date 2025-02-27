# utils.py

import json
import pandas as pd

def save_to_csv(data, filename="data/extracted_data.csv"):
    """Save data to CSV format"""
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

def save_to_json(data, filename="data/extracted_data.json"):
    """Save data to JSON format"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"Data saved to {filename}")
