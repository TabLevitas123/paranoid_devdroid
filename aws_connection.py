
import os
import psycopg2

# Retrieve AWS RDS credentials from environment variables
aws_password = os.getenv('AWS_RDS_PASSWORD')

# Secure connection to AWS RDS with proper error handling
def connect_to_aws_rds():
    try:
        connection = psycopg2.connect(
            host='database-1-instance-1.c34ewagcc44a.us-east-2.rds.amazonaws.com',
            database='prof_e_esher',
            user='postgres',
            password=aws_password
        )
        print("Secure connection to AWS RDS established!")
        return connection
    except Exception as e:
        print(f"Failed to connect to AWS RDS: {e}")
        return None
