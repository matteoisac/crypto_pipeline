import requests
from datetime import datetime

url = "https://api.binance.com/api/v3/klines"

params = {
    "symbol": "BTCUSDT",
    "interval": "1h",
    "limit": 5
}

response = requests.get(url, params=params)
response.raise_for_status()  # Raise an error if the request was unsuccessful
data = response.json()

for candle in data:
    row = {
        "timestamp": datetime.fromtimestamp(candle[0] / 1000),
        "open": float(candle[1]),
        "high": float(candle[2]),
        "low": float(candle[3]),
        "close": float(candle[4]),
        "volume": float(candle[5])
    }
    print (row)  # Print the last candle's data

