import psycopg
from extract import extract_data

rows = extract_data()

conn = psycopg.connect(
    dbname="crypto_pipeline"
)

print("Connected to PostgreSQL")
for row in rows:
    conn.execute(
        """
        INSERT INTO crypto_prices (timestamp, open, high, low, close, volume)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT (timestamp) DO NOTHING
        """,
        (
            row["timestamp"],
            row["open"],
            row["high"],
            row["low"],
            row["close"],
            row["volume"]
        )
    )

conn.commit()

conn.close()