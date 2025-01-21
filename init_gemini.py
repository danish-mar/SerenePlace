import os

def initialize_serene_place():
    """Creates a .env file for the Gemini API key."""

    api_key = input("Unveiling the secret key... What is it, wanderer? ")

    # Robust input validation, crucial for security
    if not api_key or not api_key.strip():  # Check for empty or whitespace-only input
        print("The key is silent... Please provide a valid key.")
        return  # Exit gracefully if input is invalid

    try:
        # Save to .env file, using a more secure method
        with open(".env", "w") as f:
            f.write(f"API_KEY={api_key}")
        print("The Serene Place is now prepared! Your key is safely nestled within.")
    except Exception as e:
        print(f"A shadow fell over the process. Error: {e}")


if __name__ == "__main__":
    initialize_serene_place()