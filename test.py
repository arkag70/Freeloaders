import sys
import numpy as np
from random import choice, randint
from rocket import Rocket, pygame
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
MIN_SIZE_POPULATION = 40
damp = 0.8
rockets = []
objects = []
iteration = 0

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
populationSizeList = []

# Main game loop
running = True
while running:
    iteration+=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen with a white background
    screen.fill(white)
    if len(rockets) > 0:
        averageAge = round(sum(rocket.age for rocket in rockets)/len(rockets),2)
        averageAgeList.append(averageAge)
        populationSize = len(rockets)
        populationSizeList.append(populationSize)
        oldest = max(rocket.age for rocket in rockets)
        youngest = min(rocket.age for rocket in rockets)
        print(f'''Iteration : {iteration}\tMean-age: {averageAge}\tOldest : {oldest}\tyoungest : {youngest}\tPopulation Size: {populationSize}''')
        if populationSize < MIN_SIZE_POPULATION:
            break
    for i, rocket in enumerate(rockets):
        # Draw on the canvas (for example, a red rectangle)
        try:
            pygame.draw.rect(screen, (rocket.red, rocket.green, rocket.blue), rocket.rect)
        except:
            print(f"Exception : {(rocket.red, rocket.green, rocket.blue)}")

        rocket.move()
        rocket.boundaryCheck(width, height, damp)

        if rocket.red == 255:
            rockets.remove(rocket)
        
    pygame.time.delay(delay)
    # Update the display
    pygame.display.flip()

plt.subplot(1,2,1)
plt.xlabel("Iteration")
plt.ylabel("Average Age of population")
plt.plot(list(range(len(averageAgeList))), averageAgeList, 'green')

plt.subplot(1,2,2)
plt.xlabel("Iteration")
plt.ylabel("Size of population")
plt.plot(list(range(len(populationSizeList))), populationSizeList, 'red')

plt.show()
# Quit Pygame
pygame.quit()
sys.exit()
