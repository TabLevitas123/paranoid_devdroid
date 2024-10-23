
def setup():
    print("Welcome to Marvin Setup!")
    
    # Original prompts for other APIs (let's assume AWS and Dorkle were part of the original setup)
    aws_rds_key = input("Please enter your AWS RDS Key: ")
    dorkle_api_key = input("Please enter your Dorkle API Key: ")

    # New prompts for additional API Keys
    openai_api_key = input("Please enter your OpenAI API Key: ")
    clearbit_api_key = input("Please enter your Clearbit API Key: ")
    numverify_api_key = input("Please enter your Numverify API Key: ")
    ipstack_api_key = input("Please enter your IPStack API Key: ")

    # Save all API keys to environment or config (simulated here as writing to a file for simplicity)
    with open('api_keys.txt', 'w') as f:
        f.write(f"AWS_RDS_KEY={aws_rds_key}\n")
        f.write(f"DORKLE_API_KEY={dorkle_api_key}\n")
        f.write(f"OPENAI_API_KEY={openai_api_key}\n")
        f.write(f"CLEARBIT_API_KEY={clearbit_api_key}\n")
        f.write(f"NUMVERIFY_API_KEY={numverify_api_key}\n")
        f.write(f"IPSTACK_API_KEY={ipstack_api_key}\n")

    print("Setup complete! Your API keys are saved.")

if __name__ == "__main__":
    setup()
