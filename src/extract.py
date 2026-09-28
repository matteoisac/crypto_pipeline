import requests
from datetime import datetime, timezone


def extract_data():
    url = "https://api.binance.com/api/v3/klines"

    params = {
        "symbol": "BTCUSDT",
        "interval": "1h",
        "limit": 5
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    rows = []

    for candle in data:
        row = {
            "timestamp": datetime.fromtimestamp(candle[0] / 1000, tz=timezone.utc),
            "open": float(candle[1]),
            "high": float(candle[2]),
            "low": float(candle[3]),
            "close": float(candle[4]),
            "volume": float(candle[5])
        }

        rows.append(row)

    return rows


print(extract_data())