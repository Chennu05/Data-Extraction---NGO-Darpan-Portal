# scraper.py  (Handles Web Scraping & API Extraction)

import requests
from bs4 import BeautifulSoup
import config

def fetch_ngo_data():
    """Fetch NGO data from the NGO Darpan portal"""
    response = requests.get(config.BASE_URL, headers=config.HEADERS)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data. Status Code: {response.status_code}")

    soup = BeautifulSoup(response.text, "lxml")
    ngo_list = []

    # Extracting data from the table (example)
    rows = soup.find_all("tr")[1:]  # Skip table header

    for row in rows:
        columns = row.find_all("td")
        if len(columns) > 5:  # Assuming required data exists
            ngo_data = {
                "NGO Name": columns[0].text.strip(),
                "Registration Number": columns[1].text.strip(),
                "Date of Registration": columns[2].text.strip(),
                "State": columns[3].text.strip(),
                "District": columns[4].text.strip(),
                "Contact Details": columns[5].text.strip(),
                "Type of NGO": columns[6].text.strip(),
                "Activities": columns[7].text.strip()
            }
            ngo_list.append(ngo_data)

    return ngo_list
