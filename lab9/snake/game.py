import pygame
import sys
import random
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the display
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
CELL_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // CELL_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // CELL_SIZE
BACKGROUND_COLOR = (255, 255, 255)

# Set up the game variables
FPS = 10
score = 0
level = 1
snake_speed = 10
snake_pos = [GRID_WIDTH // 2, GRID_HEIGHT // 2]
snake_body = [[snake_pos[0], snake_pos[1]], [snake_pos[0], snake_pos[1] + 1]]
food_spawn = True
direction = 'UP'
change_to = direction
food_timer = 50  # Initial food timer value
food_pos = [random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)]  # Initialize food position

# Set up Pygame window
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_UP and direction != 'DOWN':
                change_to = 'UP'
            if event.key == K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            if event.key == K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            if event.key == K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'

    # Update snake position
    if change_to == 'UP':
        snake_pos[1] -= 1
    if change_to == 'DOWN':
        snake_pos[1] += 1
    if change_to == 'LEFT':
        snake_pos[0] -= 1
    if change_to == 'RIGHT':
        snake_pos[0] += 1

    # Check for wall collision
    if snake_pos[0] < 0 or snake_pos[0] >= GRID_WIDTH or snake_pos[1] < 0 or snake_pos[1] >= GRID_HEIGHT:
        pygame.quit()
        sys.exit()

    # Check for snake body collision
    for segment in snake_body:
        if snake_pos == segment:
            pygame.quit()
            sys.exit()

    # Check for food consumption
    if snake_pos == food_pos:
        score += 1
        snake_body.append(list(food_pos))  # Add food to snake body
        food_spawn = False

    # Spawn new food
    if not food_spawn:
        food_timer -= 1
        if food_timer == 0:
            food_pos = [random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)]
            food_spawn = True
            food_timer = random.randint(50, 150)  # Randomize food timer value

    # Draw everything
    DISPLAYSURF.fill(BACKGROUND_COLOR)
    for segment in snake_body:
        pygame.draw.rect(DISPLAYSURF, (0, 255, 0), (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(DISPLAYSURF, (255, 0, 0), (food_pos[0] * CELL_SIZE, food_pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.update()

    # Cap the frame rate
    pygame.time.Clock().tick(snake_speed)
