import pygame
import sys
import numpy as np
from random import choice, randint
from rocket import Rocket
import matplotlib.pyplot as plt

delay = 30
# Define the screen dimensions
width = 800
height = 600
length = 20
breadth = 4
ayrange = axrange = np.arange(-0.01, 0.01, 0.0001, dtype=float)
vyrange = vxrange = np.arange(-10, 10, 0.1, dtype=float)
xrange = np.arange(0, width, 10, dtype=float)
xyange = np.arange(height/2, height, 10, dtype=float)
ROCKETS = 50
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
averageAgeList = []

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen with a white background
    screen.fill(white)
    if len(rockets) > 0:
        averageAge = round(sum(rocket.age for rocket in rockets)/len(rockets),2)
        averageAgeList.append(averageAge)
        oldest = max(rocket.age for rocket in rockets)
        youngest = min(rocket.age for rocket in rockets)
        print(f"Age Mean: {averageAge}\tOldest : {oldest}\tyoungest : {youngest}\tPopulation Size: {len(rockets)}")

    for i, rocket in enumerate(rockets):
        # Draw on the canvas (for example, a red rectangle)
        try:
            pygame.draw.rect(screen, (rocket.red, rocket.green, rocket.blue),
            (rocket.xpos, rocket.ypos, rocket.breadth, rocket.length))
        except:
            print(f"Exception : {(rocket.red, rocket.green, rocket.blue)}")

        rocket.move()
        rocket.boundaryCheck(width, height, damp)
        if rocket.red == 255:
            rockets.remove(rocket)
        
    pygame.time.delay(delay)
    # Update the display
    pygame.display.flip()

plt.plot(list(range(len(averageAgeList))), averageAgeList)
plt.show()
# Quit Pygame
pygame.quit()
sys.exit()
