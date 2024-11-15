import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Reptile Follows Cursor")

# Define colors
BODY_COLOR = (34, 139, 34)  # A green color for the reptile's body
LEG_COLOR = (0, 100, 0)     # Darker green for legs
HEAD_COLOR = (50, 205, 50)  # Light green for the head

# Reptile dimensions
body_width, body_height = 60, 20
head_size = 20
leg_width, leg_height = 10, 20

# Position of the reptile (centered initially)
x, y = screen_width // 2, screen_height // 2

# Main loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the current position of the mouse
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Smoothly move the reptile towards the cursor
    x += (mouse_x - x) * 0.1
    y += (mouse_y - y) * 0.1

    # Clear screen
    screen.fill((255, 255, 255))  # White background

    # Draw the body of the reptile
    body_rect = pygame.Rect(x - body_width // 2, y - body_height // 2, body_width, body_height)
    pygame.draw.rect(screen, BODY_COLOR, body_rect)

    # Draw the head of the reptile
    head_rect = pygame.Rect(x + body_width // 2, y - head_size // 2, head_size, head_size)
    pygame.draw.ellipse(screen, HEAD_COLOR, head_rect)

    # Draw legs (two at the front, two at the back)
    # Front left leg
    front_left_leg = pygame.Rect(x - body_width // 2, y - body_height // 2 - leg_height // 2, leg_width, leg_height)
    pygame.draw.rect(screen, LEG_COLOR, front_left_leg)

    # Front right leg
    front_right_leg = pygame.Rect(x - body_width // 2, y + body_height // 2 - leg_height // 2, leg_width, leg_height)
    pygame.draw.rect(screen, LEG_COLOR, front_right_leg)

    # Back left leg
    back_left_leg = pygame.Rect(x + body_width // 2 - leg_width, y - body_height // 2 - leg_height // 2, leg_width, leg_height)
    pygame.draw.rect(screen, LEG_COLOR, back_left_leg)

    # Back right leg
    back_right_leg = pygame.Rect(x + body_width // 2 - leg_width, y + body_height // 2 - leg_height // 2, leg_width, leg_height)
    pygame.draw.rect(screen, LEG_COLOR, back_right_leg)

    # Update the display
    pygame.display.flip()
    clock.tick(60)  # Limit frame rate to 60 FPS

