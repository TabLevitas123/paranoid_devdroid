
import psycopg2
import os

# AWS RDS Database details from environment variables
aws_host = os.getenv('AWS_RDS_HOST')
aws_dbname = os.getenv('AWS_RDS_DBNAME')
aws_user = os.getenv('AWS_RDS_USER')
aws_password = os.getenv('AWS_RDS_PASSWORD')

# Attempt to connect to the AWS RDS PostgreSQL instance
try:
    conn = psycopg2.connect(
        host=aws_host,
        dbname=aws_dbname,
        user=aws_user,
        password=aws_password,
        port=5432
    )
    print("Successfully connected to AWS RDS database.")
except Exception as e:
    print(f"Failed to connect to AWS RDS: {str(e)}")
