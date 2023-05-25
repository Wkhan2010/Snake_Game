import pygame
import random

# Initialize the game
pygame.init()

# Set up the game window
width, height = 640, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up the clock to control the frame rate
clock = pygame.time.Clock()

# Set up the initial position and direction of the snake
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
direction = "RIGHT"

# Set up the initial position of the food
food_position = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]
food_spawned = True

# Set up the initial score
score = 0

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    # Update snake position
    if direction == "UP":
        snake_position[1] -= 10
    elif direction == "DOWN":
        snake_position[1] += 10
    elif direction == "LEFT":
        snake_position[0] -= 10
    elif direction == "RIGHT":
        snake_position[0] += 10

    # Check for collision with the food
    if snake_position == food_position:
        score += 1
        food_spawned = False
    else:
        snake_body.insert(0, list(snake_position))
        if len(snake_body) > score + 1:
            snake_body.pop()

    # Spawn new food if necessary
    if not food_spawned:
        food_position = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]
        food_spawned = True

    # Check for collision with the boundaries
    if snake_position[0] < 0 or snake_position[0] >= width or snake_position[1] < 0 or snake_position[1] >= height:
        running = False

    # Check for collision with the snake's body
    for segment in snake_body[1:]:
        if snake_position == segment:
            running = False

    # Clear the screen
    window.fill(BLACK)

    # Draw the snake
    for segment in snake_body:
        pygame.draw.rect(window, GREEN, pygame.Rect(segment[0], segment[1], 10, 10))

    # Draw the food
    pygame.draw.rect(window, RED, pygame.Rect(food_position[0], food_position[1], 10, 10))

    # Draw the score
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, GREEN)
    window.blit(text, (10, 10))

    # Update the game display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(15)

# Quit the game
pygame.quit()
