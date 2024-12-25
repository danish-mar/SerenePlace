import os

from game.assets.properties import Mood
from game.src import MoeLogger
from colorama import Fore, Style
from game.src.generative.core import GenerativeAi
from game.assets.characters.Character import Character

def main():

    LOG_FILE = "/home/keqing/projects/SerenePlace/logs/MoeLogs.logs"

    ml = MoeLogger.MoeLogger(error_color=Fore.RED, message_color=Fore.GREEN, warning_color=Fore.YELLOW,file=LOG_FILE)

    # setting the api keys
    api_key = os.getenv("API_KEY")
    print(api_key)

    core_memory = "You are keqing a friendly and kind hearted girl suddenly stuck in a dating sim with me"

    # initializes the character
    character = Character(name="keqing", profile=core_memory,mood=Mood.NEUTRAL,api_key=api_key,ml=ml)
    character.load_from_cartridge()


    while True:
        player_message = input("Denizuh : ")
        if player_message.__contains__("/exit"):
            character.save_to_cartridge()
            exit(0)
        if player_message.__contains__("/stats"):
            print(character.mood)
        print(character.generate_response(player_message))


if __name__ == '__main__':
    main()
