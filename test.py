import pygame
import sys
import numpy as np
from random import choice, randint
from rocket import Rocket
delay = 30
# Define the screen dimensions
width = 800
height = 600
length = 20
breadth = 5
ayrange = axrange = np.arange(-0.01, 0.005, 0.0001, dtype=float)
vyrange = vxrange = np.arange(-1, 1, 0.1, dtype=float)
xrange = np.arange(0, width, 10, dtype=float)
xyange = np.arange(height/2, height, 10, dtype=float)
ROCKETS = 20
colors = [(randint(0, 255), randint(0, 255), randint(0, 255)) for _ in range(ROCKETS)]
damp = 0.8
rockets = []
objects = []
# Initialize Pygame
pygame.init()

# Create a Pygame window
screen = pygame.display.set_mode((width, height))

# Set the window title
pygame.display.set_caption("Pygame Canvas")
for _ in range(ROCKETS):
    rockets.append(Rocket(length, breadth, 
                (width/2), (height/2), 
                choice(vxrange), choice(vyrange), 
                choice(axrange), choice(ayrange)
            ))
# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
redObject = pygame.Rect(100, 100, 100, 100)
objects.append(redObject)
# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen with a white background
    screen.fill(white)
    pygame.draw.rect(screen, "red", redObject)
    for i, rocket in enumerate(rockets):
        # Draw on the canvas (for example, a red rectangle)
        pygame.draw.rect(screen, colors[i], (rocket.xpos, rocket.ypos, rocket.breadth, rocket.length))
        rocket.move()
        rocket.boundaryCheck(width, height, damp)
        
    pygame.time.delay(delay)
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
