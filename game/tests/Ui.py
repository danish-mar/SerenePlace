import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
PURPLE = (128, 0, 128)
PINK = (255, 105, 180)
WHITE = (255, 255, 255)

# Fonts
pygame.font.init()
FONT = pygame.font.Font(None, 50)
SMALL_FONT = pygame.font.Font(None, 30)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cute Game Menu")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Button properties
buttons = [
    {"text": "Enter The World", "x": SCREEN_WIDTH, "y": 250, "width": 200, "height": 60, "target_x": SCREEN_WIDTH // 2 - 100},
    {"text": "Quit", "x": SCREEN_WIDTH, "y": 350, "width": 200, "height": 60, "target_x": SCREEN_WIDTH // 2 - 100}
]
button_speed = 10


# Text rendering function
def draw_text(text, font, color, x, y, center=False):
    rendered_text = font.render(text, True, color)
    if center:
        text_rect = rendered_text.get_rect(center=(x, y))
        screen.blit(rendered_text, text_rect)
    else:
        screen.blit(rendered_text, (x, y))

# Draw button function
def draw_button(button):
    pygame.draw.rect(screen, PINK, (button["x"], button["y"], button["width"], button["height"]), border_radius=15)
    draw_text(button["text"], SMALL_FONT, WHITE, button["x"] + button["width"] // 2, button["y"] + button["height"] // 2, center=True)

# Main menu function
def main_menu():
    global image_alpha

    running = True
    while running:
        screen.fill(PURPLE)

        # Animate buttons
        for button in buttons:
            if button["x"] > button["target_x"]:
                button["x"] -= button_speed



        # Draw buttons
        for button in buttons:
            draw_button(button)



        # Draw the title
        draw_text("Serene Place", FONT, WHITE, SCREEN_WIDTH // 2, 100, center=True)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # Check button clicks
                if buttons[0]["x"] <= mouse_pos[0] <= buttons[0]["x"] + buttons[0]["width"] and \
                        buttons[0]["y"] <= mouse_pos[1] <= buttons[0]["y"] + buttons[0]["height"]:
                    print("Start Game Clicked!")
                if buttons[1]["x"] <= mouse_pos[0] <= buttons[1]["x"] + buttons[1]["width"] and \
                        buttons[1]["y"] <= mouse_pos[1] <= buttons[1]["y"] + buttons[1]["height"]:
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        clock.tick(60)

# Run the menu
main_menu()
