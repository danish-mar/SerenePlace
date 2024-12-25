import pickle
import os

from game.assets.properties import Mood
from game.src.generative import GenerativeAi


class Character:
    def __init__(self, name, profile, mood, api_key, ml, model="gemini-1.5-flash"):
        """
        Initializes the Character class with profile and mood, and integrates the Generative AI.

        :param name: The name of the character
        :param profile: Profile information for the character (name, description, etc.)
        :param mood: The current mood of the character (happy, sad, etc.)
        :param api_key: The API key for the generative AI
        :param ml: An instance of MoeLogger to handle logging
        :param model: The model name for the AI (default is "gemini-1.5-flash")
        :param core_memory: The core memory (context) for the AI
        """
        self.name = name
        self.profile = profile
        self.mood = mood
        self.ml = ml
        self.history = []

        # Initialize GenerativeAi

        self.ai = GenerativeAi(api_key=api_key, model=model, core_memory=profile, ml=ml)

    def generate_shortest_summart(self,message):
        return GenerativeAi.generate_response("make a shortest summart for this : " + message)

    def generate_response(self, player_message):
        """
        Generates a response from the character using the generative AI based on the player's message.

        :param player_message: The message from the player to the character
        :return: The AI-generated response
        """
        context = f"{self.profile}\nMood: {self.mood}\n"
        full_message = context + player_message
        ai_response = self.ai.generate_response(full_message)

        # Log and return the response
        self.ml.message(f"Character Response: {ai_response}")

        # Update the character's mood based on the response
        self.update_mood(ai_response)

        #self.history.append(player_message + " : " + ai_response)
        self.history = self.ai.get_chat_history()


        return ai_response

    def update_mood(self, ai_response):
        """
        Update the character's mood based on the AI response.
        """
        mood_mapping = {
            "angry": Mood.ANGRY,
            "happy": Mood.HAPPY,
            "sad": Mood.SAD,
            "blushing": Mood.BLUSHING,
            "craving": Mood.CRAVING,
            "irritated": Mood.IRRITATED,
            "affection": Mood.AFFECTIONATE
        }

        detected_mood = next((mood_mapping[key] for key in mood_mapping if key in ai_response.lower()), Mood.NEUTRAL)
        self.mood = detected_mood
        self.ml.message(f"Character's Mood is now: {self.mood.value}")

    def save_to_cartridge(self):
        """
        Saves the character's state (name, profile, mood, history) to a file.
        Logs the action using MoeLogger.
        """
        try:
            character_data = {
                "name": self.name,
                "profile": self.profile,
                "mood": self.mood,
                "history": self.history
            }

            # Create a directory to save if it doesn't exist
            if not os.path.exists('saves'):
                os.makedirs('saves')

            file_name = f'saves/character_{self.name.lower().replace(" ", "_")}_cartridge.pkl'
            with open(file_name, 'wb') as file:
                pickle.dump(character_data, file)
        except Exception as e:
            self.ml.error(f"Failed to save character data: {e}")

    def load_from_cartridge(self):
        """
        Loads the character's state from a file.
        Logs the action using MoeLogger.
        """
        try:
            file_name = f'saves/character_{self.name.lower().replace(" ", "_")}_cartridge.pkl'

            if os.path.exists(file_name):
                with open(file_name, 'rb') as file:
                    character_data = pickle.load(file)
                    self.name = character_data["name"]
                    self.profile = character_data["profile"]
                    self.mood = character_data["mood"]
                    self.history = character_data["history"]
                    print(self.history)
                    self.ml.message(f"Character data loaded for {self.name} from {file_name}")
                    self.ai.reboot(self.history)

            else:
                self.ml.warning(f"No saved data found for character {self.name}")
        except Exception as e:
            self.ml.error(f"Failed to load character data: {e}")
