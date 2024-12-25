import pickle
import os


class PlayerCartrige:
    def __init__(self, player_id, player_name, player_age, player_gender, logger):
        """
        Initializes the PlayerCartrige class with player details and logger.

        :param player_id: Unique ID for the player
        :param player_name: Name of the player
        :param player_age: Age of the player
        :param player_gender: Gender of the player
        :param logger: An instance of the MoeLogger class
        """
        self.player_id = player_id
        self.player_name = player_name
        self.player_age = player_age
        self.player_gender = player_gender
        self.logger = logger
        self.file_name = f"player_{self.player_id}_cartridge.pkl"

    def save_cartridge(self):
        """
        Saves the player's data to a file using pickle serialization.
        Logs the action using MoeLogger.
        """
        try:
            player_data = {
                "player_id": self.player_id,
                "player_name": self.player_name,
                "player_age": self.player_age,
                "player_gender": self.player_gender
            }

            # Create a directory to save if it doesn't exist
            if not os.path.exists('saves'):
                os.makedirs('saves')

            # Save the player data to a file
            with open(f'saves/{self.file_name}', 'wb') as file:
                pickle.dump(player_data, file)
                self.logger.message(f"Player data saved for {self.player_name} in {self.file_name}")
        except Exception as e:
            self.logger.error(f"Failed to save player data: {e}")

    def load_cartridge(self):
        """
        Loads the player's data from a file.
        Logs the action using MoeLogger.
        """
        try:
            # Check if the save file exists
            if os.path.exists(f'saves/{self.file_name}'):
                with open(f'saves/{self.file_name}', 'rb') as file:
                    player_data = pickle.load(file)
                    self.player_id = player_data["player_id"]
                    self.player_name = player_data["player_name"]
                    self.player_age = player_data["player_age"]
                    self.player_gender = player_data["player_gender"]
                    self.logger.message(f"Player data loaded for {self.player_name} from {self.file_name}")
            else:
                self.logger.warning(f"No saved data found for player ID {self.player_id}")
        except Exception as e:
            self.logger.error(f"Failed to load player data: {e}")
#
#
#
# # Example usage
# logger = MoeLogger(file="logs/MoeLogs.logs", version="V1.0.0", debug=True)
#
# # Create a player instance
# player = PlayerCartrige(player_id=1, player_name="Denizuh", player_age=20, player_gender="Male", logger=logger)
# player.save_cartridge()  # Save the game
#
# # Later or in another session
# new_player = PlayerCartrige(player_id=1, player_name="", player_age=0, player_gender="", logger=logger)
# new_player.load_cartridge()  # Load the saved game
#
# # Output loaded player data
# print(f"Loaded player: {new_player.player_name}, Age: {new_player.player_age}, Gender: {new_player.player_gender}")
