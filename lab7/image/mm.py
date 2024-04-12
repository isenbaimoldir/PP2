import pygame
import os
import math
import time

pygame.init()

# Load images
mickey_image = pygame.image.load('mickeyimage.png')  # Mickey Mouse image
right_hand_image = pygame.image.load('right.png')  # Right hand image
left_hand_image = pygame.image.load('left.png')  # Left hand image

# Set initial positions
window_size = (400, 300)
screen = pygame.display.set_mode(window_size)
mickey_rect = mickey_image.get_rect(center=(window_size[0] // 2, window_size[1] // 2))
right_hand_rect = right_hand_image.get_rect(center=(mickey_rect.centerx + 40, mickey_rect.centery))
left_hand_rect = left_hand_image.get_rect(center=(mickey_rect.centerx - 40, mickey_rect.centery))

# Setup rotation angles
right_hand_angle = 0
left_hand_angle = 0

def update_angles():
    global right_hand_angle, left_hand_angle
    current_time = time.localtime()
    right_hand_angle = (current_time.tm_min / 60) * 360  # Minute hand
    left_hand_angle = (current_time.tm_sec / 60) * 360  # Second hand

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    update_angles()

    screen.fill((255, 255, 255))

    # Draw Mickey Mouse
    screen.blit(mickey_image, mickey_rect)

    # Rotate and draw the right hand
    rotated_right_hand = pygame.transform.rotate(right_hand_image, -right_hand_angle)
    rotated_right_hand_rect = rotated_right_hand.get_rect(center=right_hand_rect.center)
    screen.blit(rotated_right_hand, rotated_right_hand_rect)

    # Rotate and draw the left hand
    rotated_left_hand = pygame.transform.rotate(left_hand_image, -left_hand_angle)
    rotated_left_hand_rect = rotated_left_hand.get_rect(center=left_hand_rect.center)
    screen.blit(rotated_left_hand, rotated_left_hand_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
