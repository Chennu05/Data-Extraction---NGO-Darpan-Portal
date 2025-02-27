## Features
- **Automated Web Scraping & API Extraction**: Fetch NGO details efficiently.
- **Data Cleaning & Validation**: Removes duplicates and ensures structured data.
- **Multiple Output Formats**: Supports CSV, JSON, and database storage.
- **Scalable & Efficient**: Handles pagination and rate limiting.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ngo-darpan-data-extraction.git
   cd ngo-darpan-data-extraction
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the main script to extract and save data:
```bash
python src/main.py
```

## Folder Structure
```
ngo-darpan-data-extraction/
│── README.md
│── src/
│   ├── main.py          # Runs the entire process
│   ├── scraper.py       # Handles data extraction
│   ├── data_cleaning.py # Cleans and validates data
│   ├── config.py        # Stores configurations
│── data/
│   ├── extracted_data.csv
│   ├── extracted_data.json
│── requirements.txt
│── .gitignore
```

## Configuration
Edit **config.py** to update **URLs, API keys, or output formats**.

## Output Example
```json
{
    "NGO Name": "Example NGO",
    "Registration Number": "123456",
    "Date of Registration": "2022-05-15",
    "State": "Maharashtra",
    "District": "Mumbai",
    "Contact Details": "example@email.com",
    "Type of NGO": "Society",
    "Activities": "Education, Healthcare"
}
```
