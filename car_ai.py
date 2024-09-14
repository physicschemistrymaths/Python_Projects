import pygame
import time

# Initialize Pygame
pygame.init()

# Set up the display
display_width = 800
display_height = 600
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Car Game')

# Set up the car image
car_image = pygame.image.load('car.png')  # Replace 'car.png' with the actual image file path
car_width = 73

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()
car_speed = 0

def car(x, y):
    game_display.blit(car_image, (x, y))

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            # Move the car
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        game_display.fill(white)
        car(x, y)

        if x > display_width - car_width or x < 0:
            game_exit = True

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

# Run the game
game_loop()
