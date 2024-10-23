
import psycopg2

# AWS RDS Database details
aws_host = "YOUR_AWS_HOST"
aws_dbname = "YOUR_DB_NAME"
aws_user = "YOUR_DB_USER"
aws_password = "YOUR_DB_PASSWORD"

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
