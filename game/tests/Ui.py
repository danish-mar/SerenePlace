import pygame
import json
from game.assets.Ui.KawaiUi import UiFactory

# Initialize Pygame
pygame.init()

# Load the theme from the JSON file
with open('game/data/Theme.json') as theme_file:
    theme = json.load(theme_file)["theme"]

# Create a screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("UI Factory Example")

# Create an instance of UiFactory
ui_factory = UiFactory(theme)

# Create a button and a label
button = ui_factory.create_button("Click Me", (100, 100), (200, 50))

label = ui_factory.create_label("Hello, World!", (100, 200), 24)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(theme["colors"]["background"])

    # Draw the button and the label
    ui_factory.draw_button(screen, button)

    ui_factory.draw_label(screen, label)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()