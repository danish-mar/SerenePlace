import pickle
import os

class CharacterCartridge:
    def __init__(self, character, logger):
        """
        Initializes the CharacterCartridge class with a character instance and logger.

        :param character: An instance of the Character class
        :param logger: An instance of the MoeLogger class
        """
        self.character = character
        self.logger = logger
        self.file_name = f"character_{self.character.name.lower().replace(' ', '_')}_cartridge.pkl"

    def save_cartridge(self):
        """
        Saves the character's state (name, profile, mood, history) to a file.
        Logs the action using MoeLogger.
        """
        try:
            character_data = {
                "name": self.character.name,
                "profile": self.character.profile,
                "mood": self.character.mood,
                "history": self.character.history
            }

            # Create a directory to save if it doesn't exist
            if not os.path.exists('saves'):
                os.makedirs('saves')

            # Save the character data to a file
            with open(f'saves/{self.file_name}', 'wb') as file:
                pickle.dump(character_data, file)
                self.logger.message(f"Character data saved for {self.character.name} in {self.file_name}")
        except Exception as e:
            self.logger.error(f"Failed to save character data: {e}")

    def load_cartridge(self):
        """
        Loads the character's state from a file.
        Logs the action using MoeLogger.
        """
        try:
            # Check if the save file exists
            if os.path.exists(f'saves/{self.file_name}'):
                with open(f'saves/{self.file_name}', 'rb') as file:
                    character_data = pickle.load(file)
                    self.character.name = character_data["name"]
                    self.character.profile = character_data["profile"]
                    self.character.mood = character_data["mood"]
                    self.character.history = character_data["history"]
                    self.logger.message(f"Character data loaded for {self.character.name} from {self.file_name}")
            else:
                self.logger.warning(f"No saved data found for character {self.character.name}")
        except Exception as e:
            self.logger.error(f"Failed to load character data: {e}")
