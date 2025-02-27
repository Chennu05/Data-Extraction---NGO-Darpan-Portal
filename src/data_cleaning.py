# data_cleaning.py  (Cleans & Validates Data)
 
import pandas as pd

def clean_data(data):
    """Clean and validate extracted NGO data"""
    df = pd.DataFrame(data)

    # Drop duplicates
    df.drop_duplicates(inplace=True)

    # Convert date to proper format
    df["Date of Registration"] = pd.to_datetime(df["Date of Registration"], errors="coerce")

    # Remove invalid email addresses (if available in contact details)
    df["Contact Details"] = df["Contact Details"].apply(lambda x: x if "@" in x else None)

    return df
