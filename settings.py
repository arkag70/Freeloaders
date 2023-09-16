import numpy as np
# Define the screen dimensions
width = 800
height = 600
length = 20
breadth = 5
ayrange = axrange = np.arange(-0.01, 0.01, 0.0001, dtype=float)
vyrange = vxrange = np.arange(-10, 10, 0.1, dtype=float)
xrange = np.arange(0, width, 10, dtype=float)
xyange = np.arange(height/2, height, 10, dtype=float)
FREELOADERS = 400
MIN_SIZE_POPULATION = 0.1 * FREELOADERS
damp = 0.8
freeloaders = []
objects = []
iteration = 0
delay = 30
averageAgeList = []
populationSizeList = []
# Define colors
white = (255, 255, 255)
black = (0, 0, 0)