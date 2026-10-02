import boto3


def load_to_redshift():
    client = boto3.client(
        "redshift-data",
        region_name="us-east-1"
    )

    sql = """
    TRUNCATE TABLE public.crypto_prices;

    COPY public.crypto_prices
    FROM 's3://matteoisac-crypto-pipeline/crypto_prices.csv'
    IAM_ROLE 'arn:aws:iam::721274598530:role/service-role/AmazonRedshift-CommandsAccessRole-20261002T161459'
    FORMAT AS CSV
    IGNOREHEADER 1
    TIMEFORMAT 'auto';
    """

    response = client.execute_statement(
        WorkgroupName="crypto-pipeline-workgroup",
        Database="dev",
        Sql=sql
    )

    print("Redshift statement submitted:", response["Id"])