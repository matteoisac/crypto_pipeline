import psycopg

conn = psycopg.connect(
    dbname="crypto_pipeline"
)

print("Connected to PostgreSQL")

conn.close()