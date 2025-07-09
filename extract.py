# utils/extract.py

import requests
import pandas as pd

def extract_data_from_api(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Akan memunculkan error kalau response bukan 200 OK
        data = response.json()
        return pd.DataFrame(data)  # Langsung ubah ke DataFrame
    except requests.exceptions.RequestException as e:
        print(f"Terjadi error saat mengambil data: {e}")
        return pd.DataFrame()
