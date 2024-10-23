
def setup():
    print("Welcome to Marvin Setup!")
    
    # Prompt for Dorkle API Key
    dorkle_api_key = input("Please enter your Dorkle API Key: ")

    # Save API key to environment or config (simulated here as writing to a file for simplicity)
    with open('api_keys.txt', 'w') as f:
        f.write(f"DORKLE_API_KEY={dorkle_api_key}\n")

    print("Setup complete! Your API keys are saved.")

if __name__ == "__main__":
    setup()
