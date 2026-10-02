import os
import psycopg
import csv
import boto3


def export_to_csv():

    conn = psycopg.connect(
        dbname="crypto_pipeline",
        user="postgres",
        password=os.getenv("POSTGRES_PASSWORD"),
        host="postgres",
        port=5432
    )

    cursor = conn.cursor()

    cursor.execute("""
        SELECT timestamp, open, high, low, close, volume
        FROM crypto_prices
        ORDER BY timestamp;
    """)

    rows = cursor.fetchall()

    with open("/tmp/crypto_prices.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "timestamp", "open", "high", "low", "close", "volume"
        ])

        writer.writerows(rows)

    cursor.close()
    conn.close()


def upload_to_s3():
    s3 = boto3.client("s3")

    s3.upload_file(
        "/tmp/crypto_prices.csv",
        "matteoisac-crypto-pipeline",
        "crypto_prices.csv"
    )

    print("File uploaded to S3")