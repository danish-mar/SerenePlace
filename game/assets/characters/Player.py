from game.assets.properties.moods import mood


class Character:
    """
        Base class for character
    """

    def __init__(self, id, name):
        """
        Initializes a Character Object
        """
        self.name = name
        self.id = id
        self.mood = mood.NEUTRAL
        