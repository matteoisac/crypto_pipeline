import requests

url = "https://api.binance.com/api/v3/klines"

params = {
    "symbol": "BTCUSDT",
    "interval": "1h",
    "limit": 5
}

response = requests.get(url, params=params)
data = response.json()

for candle in data:
    row = {
        "timestamp": candle[0],
        "open": candle[1],
        "high": candle[2],
        "low": candle[3],
        "close": candle[4],
        "volume": candle[5]
    }
    print (row)  # Print the last candle's data

# print(candle[0], candle[1], candle[2], candle[3], candle[4], candle[5])  # Print timestamp, open price, high price, low price, close price, volume