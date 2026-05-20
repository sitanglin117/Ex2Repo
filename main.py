"""
Reproducible Research Demo
"""

import pandas as pd
import requests


def load_and_summarize_csv():
    """Create a small sample dataset and print a summary."""
    data = {
        "country": ["Poland", "Germany", "France", "Italy", "Spain"],
        "population_millions": [38.0, 83.2, 67.4, 59.0, 47.4],
        "gdp_per_capita_usd": [18_894, 48_432, 43_659, 34_776, 29_614],
        "year": [2023, 2023, 2023, 2023, 2023],
    }

    df = pd.DataFrame(data)

    print("=== Dataset ===")
    print(df.to_string(index=False))

    print("\n=== Summary Statistics ===")
    print(df.describe().round(2))

    print(f"\nCountry with highest GDP per capita: "
          f"{df.loc[df['gdp_per_capita_usd'].idxmax(), 'country']}")
    print(f"Total population in dataset: "
          f"{df['population_millions'].sum():.1f} million")

    return df


def fetch_public_data():
    """Fetch a simple public JSON endpoint and display results."""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 52.23,   # Warsaw
        "longitude": 21.01,
        "current": "temperature_2m,wind_speed_10m",
        "timezone": "Europe/Warsaw",
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        current = data["current"]
        print("\n=== Current Weather in Warsaw ===")
        print(f"Temperature : {current['temperature_2m']} °C")
        print(f"Wind speed  : {current['wind_speed_10m']} km/h")
    except requests.RequestException as exc:
        print(f"\n[Note] Could not reach weather API: {exc}")


if __name__ == "__main__":
    load_and_summarize_csv()
    fetch_public_data()
