import pandas as pd
from fredapi import Fred
from config import FRED_API_KEY
fred = Fred(api_key=FRED_API_KEY)
HOUSING_MARKETS = {
    "Los Angeles": "LXXRSA",
    "San Francisco": "SFXRSA",
    "San Diego": "SDXRSA",
    "Las Vegas": "LVXRSA",
    "Phoenix": "PHXRSA",
    "Seattle": "SEXRSA",
    "Denver": "DNXRSA",
    "Miami": "MIXRSA",
    "New York": "NYXRSA",
    "Chicago": "CHXRSA",
    "Boston": "BOXRSA",
    "Washington DC": "WDXRSA"
}
def load_housing_data(selected_city=None):
    print("Loading housing data...")
    all_data = {}

    markets = HOUSING_MARKETS

    if selected_city:
        markets = {
            selected_city: HOUSING_MARKETS[selected_city]
        }

    for city, series_id in markets.items():

        print(f"Requesting {city} data...")

        data = fred.get_series(series_id)

        all_data[city] = data

        print(f"{city}: {len(data)} months received")
    df = pd.DataFrame(all_data)
    return df