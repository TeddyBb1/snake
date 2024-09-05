import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Screen dimensions
screen_width = 800  # Increased width for better space
screen_height = 600  # Increased height for better space

# Define block size
block_size = 20  # Snake and food block size
snake_speed = 15

# Initialize the game window
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

# Clock for controlling speed
clock = pygame.time.Clock()

# Font for displaying messages and score
font_style = pygame.font.SysFont("bahnschrift", 35)
score_font = pygame.font.SysFont("comicsansms", 25)

# Function to display the score
def display_score(score):
    score_text = score_font.render(f"Score: {score}", True, white)
    window.blit(score_text, [0, 0])

# Function to display centered message
def message(msg, color):
    message_text = font_style.render(msg, True, color)
    text_rect = message_text.get_rect(center=(screen_width / 2, screen_height / 2))
    window.blit(message_text, text_rect)

def game():
    # Initial coordinates of the snake
    snake_x = screen_width / 2
    snake_y = screen_height / 2

    # Movement changes
    x_change = 0
    y_change = 0

    # Snake's body list and initial length
    snake_body = []
    snake_length = 1

    # Food coordinates (aligned to grid)
    food_x = round(random.randrange(0, screen_width - block_size) / block_size) * block_size
    food_y = round(random.randrange(0, screen_height - block_size) / block_size) * block_size

    # Game state
    game_over = False
    game_running = True

    # Score tracking
    score = 0

    while game_running:

        while game_over:
            window.fill(blue)
            message("You lost! Press Q to Quit or C to Play Again", red)
            pygame.display.update()

            # Event handling after the game is over
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_running = False
                        game_over = False
                    if event.key == pygame.K_c:
                        game()

        # Event handling for movement
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -block_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = block_size
                    x_change = 0

        # Update snake position
        if snake_x >= screen_width or snake_x < 0 or snake_y >= screen_height or snake_y < 0:
            game_over = True
        snake_x += x_change
        snake_y += y_change
        window.fill(black)

        # Draw food (aligned to the grid)
        pygame.draw.rect(window, green, [food_x, food_y, block_size, block_size])

        # Update snake's body
        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_body.append(snake_head)
        if len(snake_body) > snake_length:
            del snake_body[0]

        # Check if snake collides with itself
        for segment in snake_body[:-1]:
            if segment == snake_head:
                game_over = True

        # Draw the snake
        for segment in snake_body:
            pygame.draw.rect(window, white, [segment[0], segment[1], block_size, block_size])

        # Update the game window
        pygame.display.update()

        # Check if snake eats the food (aligned check)
        if snake_x == food_x and snake_y == food_y:
            food_x = round(random.randrange(0, screen_width - block_size) / block_size) * block_size
            food_y = round(random.randrange(0, screen_height - block_size) / block_size) * block_size
            snake_length += 1
            score += 1

        # Display the score
        display_score(score)

        # Control game speed
        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
game()
