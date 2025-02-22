import os

from game.assets.properties import Mood
from game.src import MoeLogger
from colorama import Fore, Style
from game.src.generative.core import GenerativeAi
from game.assets.characters.Character import Character
from dotenv import load_dotenv


def main():
    LOG_FILE = "moe.logs"

    ml = MoeLogger.MoeLogger(error_color=Fore.RED, message_color=Fore.GREEN, warning_color=Fore.YELLOW, file=LOG_FILE)

    # Load environment variables from .env file
    load_dotenv()

    # Now access the API key:
    api_key = os.getenv('API_KEY')

    if api_key:
        print("API Key loaded successfully!")

    else:
        print("API Key error")
        exit(1)  # Exit with an error code

    # setting up player
    player_name = input("Please Enter Your Name to log Back in! : ")
    print(player_name)

    core_memory = f"You are keqing a friendly and kind hearted girl suddenly stuck in a dating sim with {player_name}"
    print(core_memory)

    # initializes the character
    character = Character(name="keqing", profile=core_memory, mood=Mood.NEUTRAL, api_key=api_key, ml=ml)
    character.load_from_cartridge()

    while True:
        player_message = input(f"{player_name} : ")
        if player_message.__contains__("/exit"):
            print(character.generate_response(f"{player_name} is glitching out of the world disconnecting, leaving"))
            character.save_to_cartridge()
            exit(0)
        if player_message.__contains__("/stats"):
            print(character.mood)
        print(character.generate_response(player_message))


if __name__ == '__main__':
    main()
