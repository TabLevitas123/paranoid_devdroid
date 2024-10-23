
def setup():
    print("Welcome to Marvin Setup!")

    # Prompt for various API Keys
    openai_api_key = input("Please enter your OpenAI API Key: ")
    clearbit_api_key = input("Please enter your Clearbit API Key: ")
    numverify_api_key = input("Please enter your Numverify API Key: ")
    ipstack_api_key = input("Please enter your IPStack API Key: ")

    # Save API keys to environment or config (simulated here as writing to a file for simplicity)
    with open('api_keys.txt', 'w') as f:
        f.write(f"OPENAI_API_KEY={openai_api_key}\n")
        f.write(f"CLEARBIT_API_KEY={clearbit_api_key}\n")
        f.write(f"NUMVERIFY_API_KEY={numverify_api_key}\n")
        f.write(f"IPSTACK_API_KEY={ipstack_api_key}\n")

    print("Setup complete! Your API keys are saved.")

if __name__ == "__main__":
    setup()
