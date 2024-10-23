
def setup():
    print("Welcome to Marvin Setup!")
    print("Marvin is here to assist you with every step of your AI journey.")

    # Original prompts for API keys or other configurations (assuming AWS RDS and Dorkle API were already in place)
    aws_rds_key = input("Please enter your AWS RDS Key: ")
    dorkle_api_key = input("Please enter your Dorkle API Key: ")

    # Adding the new API prompts for OpenAI, Clearbit, Numverify, and IPStack
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

    print("Setup complete! Marvin is now ready to assist with full verification capabilities.")

if __name__ == "__main__":
    setup()
