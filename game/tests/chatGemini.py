import os
import google.generativeai as genai
from game.src.MoeLogger import MoeLogger
from colorama import Fore, Style
from game.assets.characters.Character import Character
from game.src.MoeLogger import MoeLogger

# Example usage
if __name__ == "__main__":
    # Initialize MoeLogger for logging
    ml = MoeLogger.MoeLogger(error_color=Fore.RED, message_color=Fore.GREEN, warning_color=Fore.YELLOW,version="V0.0.1")

    # Set your API key and core memory for the generative AI model
    #api_key = "your_api_key_here"
    api_key = os.environ.get("API_KEY")

    core_memory = "You are a friendly and kind character in a dating simulation."

    # Initialize the Character with profile and mood
    character = Character(profile="You are Keqing, Yuheng of the liyue qixing, u moods is defined by putting mood inside astresks, like *blushing* etc ", mood="happy", api_key=api_key, ml=ml)

    # Player message
    player_message = "Oye babe, how are you doin..."

    # Generate the character's response
    response = character.generate_response(player_message)
    print(response)



# if __name__ == "__main__":
#     gemini_api_key = os.environ.get("API_KEY")
#     genAi = GenerativeAi(gemini_api_key,core_memory="You are keqing, u are a virtual companion or maybe yandere in this realm with denizuh ur messages are conversational with only facial emotions covered in * like blusing, sad etc")
#     print(genAi.generate_response(f"Using Sofa + pouting at user"))
#     print(genAi.generate_response(f"what did u just said?"))
