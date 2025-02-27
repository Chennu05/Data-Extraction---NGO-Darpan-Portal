# main.py

import scraper
import data_cleaning
import config
import pandas as pd
import json

def save_data(data):
    """Save cleaned data in CSV or JSON format"""
    if config.OUTPUT_FORMAT == "csv":
        data.to_csv("data/extracted_data.csv", index=False)
        print("Data saved as CSV")
    else:
        data.to_json("data/extracted_data.json", orient="records", indent=4)
        print("Data saved as JSON")

def main():
    print("Fetching NGO Data...")
    raw_data = scraper.fetch_ngo_data()

    print("Cleaning Data...")
    cleaned_data = data_cleaning.clean_data(raw_data)

    print("Saving Data...")
    save_data(cleaned_data)

    print("Process Completed Successfully!")

if __name__ == "__main__":
    main()
