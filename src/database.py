# database.py

import psycopg2
import config

def save_to_database(data):
    """Save extracted NGO data into PostgreSQL database"""
    conn = psycopg2.connect(**config.DB_CONFIG)
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ngos (
            ngo_name TEXT,
            registration_number TEXT,
            date_of_registration DATE,
            state TEXT,
            district TEXT,
            contact_details TEXT,
            type_of_ngo TEXT,
            activities TEXT
        )
    """)

    # Insert data
    for ngo in data:
        cursor.execute("""
            INSERT INTO ngos (ngo_name, registration_number, date_of_registration, state, district, contact_details, type_of_ngo, activities)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            ngo["NGO Name"], ngo["Registration Number"], ngo["Date of Registration"],
            ngo["State"], ngo["District"], ngo["Contact Details"],
            ngo["Type of NGO"], ngo["Activities"]
        ))

    conn.commit()
    cursor.close()
    conn.close()
    print("Data saved to PostgreSQL database")
