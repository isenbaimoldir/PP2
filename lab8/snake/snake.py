import pygame
import sys
import random
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the display
width = 400
height = 400
cell_size = 20
grid_width = width // cell_size
grid_height = height // cell_size
colour = (0, 0, 0)
bg_colour = (255, 255, 255)

# Set up the game variables
FPS = 10
score = 0
level = 1
snake_speed = 10
snake_pos = [grid_width // 2, grid_height // 2]
snake_body = [[snake_pos[0], snake_pos[1]], [snake_pos[0], snake_pos[1] + 1]]
food_pos = [random.randint(0, grid_width - 1), random.randint(0, grid_height - 1)]
food_spawn = True
direction = 'UP'
change_to = direction

# Set up Pygame window
DISPLAYSURF = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                change_to = 'UP'
            if event.key == K_DOWN:
                change_to = 'DOWN'
            if event.key == K_LEFT:
                change_to = 'LEFT'
            if event.key == K_RIGHT:
                change_to = 'RIGHT'

    # Validate the direction input
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Update snake position
    if direction == 'UP':
        snake_pos[1] -= 1
    if direction == 'DOWN':
        snake_pos[1] += 1
    if direction == 'LEFT':
        snake_pos[0] -= 1
    if direction == 'RIGHT':
        snake_pos[0] += 1

    # Check for wall collision
    if snake_pos[0] < 0 or snake_pos[0] >= grid_width or snake_pos[1] < 0 or snake_pos[1] >= grid_height:
        pygame.quit()
        sys.exit()

    # Check for snake body collision
    for segment in snake_body:
        if snake_pos == segment:
            pygame.quit()
            sys.exit()

    # Check for food consumption
    if snake_pos == food_pos:
        food_spawn = False
        score += 1
    else:
        snake_body.pop()

    # Spawn new food
    if not food_spawn:
        food_pos = [random.randint(0, grid_width - 1), random.randint(0, grid_height - 1)]
        food_spawn = True

    # Update snake body
    snake_body.insert(0, list(snake_pos))

    # Level up based on score
    if score >= 3:
        level = 2
        snake_speed = 15

    # Draw everything
    DISPLAYSURF.fill(bg_colour)
    for segment in snake_body:
        pygame.draw.rect(DISPLAYSURF, (0, 255, 0), (segment[0] * cell_size, segment[1] * cell_size, cell_size, cell_size))
    pygame.draw.rect(DISPLAYSURF, (255, 0, 0), (food_pos[0] * cell_size, food_pos[1] * cell_size, cell_size, cell_size))
    pygame.display.update()

    # Cap the frame rate
    pygame.time.Clock().tick(snake_speed)
