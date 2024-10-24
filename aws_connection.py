
import os
import psycopg2

# Securely retrieve the AWS RDS credentials using environment variables
aws_password = os.getenv('AWS_RDS_PASSWORD')

# Placeholder replacement - making sure connection parameters are secure and error-handled
def connect_to_aws_rds():
    try:
        connection = psycopg2.connect(
            host='database-1-instance-1.c34ewagcc44a.us-east-2.rds.amazonaws.com',
            database='prof_e_esher',
            user='postgres',
            password=aws_password  # Ensure this is properly retrieved from the environment
        )
        print("Connection to AWS RDS successful!")
        return connection
    except Exception as e:
        print(f"Error connecting to AWS RDS: {e}")
        return None
