import numpy as np
# Define the screen dimensions

def getRange(params):
    start, stop, step = params
    return np.arange(start, stop, step, dtype=float)

width = 800
height = 600
length = 20
breadth = 5

accParams = (-0.01, 0.01, 0.0001)
veclParams = (-5, 5, 0.01)
xposParams = (0, width, 10)
yposparams = (height/2, height, 10)
FREELOADERS = 1000
MIN_POPULATION_SIZE = 0.05 * FREELOADERS
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
