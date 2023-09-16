import sys
from random import choice
from freeloader import Freeloader, pygame
import threading
from settings import *
from chart import *

def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("music/theme.mp3")  # Replace with your music file
    pygame.mixer.music.set_volume(0.05)  # Adjust the volume as needed
    pygame.mixer.music.play(-1)  # -1 indicates infinite loop

if __name__ == "__main__":
    # Initialize Pygame
    pygame.init()

    music_thread = threading.Thread(target=play_music)
    music_thread.daemon = True  # This will allow the program to exit even if the thread is running
    music_thread.start()

    # Create a Pygame window
    screen = pygame.display.set_mode((width, height))

    # Set the window title
    pygame.display.set_caption("Pygame Canvas")
    for _ in range(FREELOADERS):
        freeloaders.append(Freeloader(length, breadth, 
            (choice(getRange(xposParams))), choice(getRange(yposparams)), 
            choice(getRange(veclParams)), choice(getRange(veclParams)), 
            choice(getRange(accParams)), choice(getRange(accParams))))

    # Main game loop
    running = True
    while running:
        iteration+=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        numFreeloaders = len(freeloaders)

        # Clear the screen with a white background
        screen.fill(white)
        if numFreeloaders > 0:
            averageAge = round(sum(freeloader.age for freeloader in freeloaders)/numFreeloaders,2)
            averageAgeList.append(averageAge)
            populationSize = numFreeloaders
            populationSizeList.append(populationSize)
            oldest = max(freeloader.age for freeloader in freeloaders)
            youngest = min(freeloader.age for freeloader in freeloaders)
            print(f'''Iteration : {iteration}\tMean-age: {averageAge}\tOldest : {oldest}\tyoungest : {youngest}\tPopulation Size: {populationSize}''')
            
        if populationSize < MIN_POPULATION_SIZE:
            break

        for i, freeloader in enumerate(freeloaders):
            # Draw on the canvas (for example, a red rectangle)
            try:
                pygame.draw.rect(screen, (freeloader.red, freeloader.green, freeloader.blue), freeloader.rect)
            except:
                print(f"Exception : {(freeloader.red, freeloader.green, freeloader.blue)}")

            freeloader.move()
            freeloader.boundaryCheck(width, height, damp)

            if freeloader.red == 255:
                freeloaders.remove(freeloader)
            
        pygame.time.delay(delay)
        # Update the display
        pygame.display.flip()
    plotChart(averageAgeList, "iteration", "Population Age", "", "green", (1,2,1))
    plotChart(populationSizeList, "iteration", "Population Size", "", "red", (1,2,2))
    viewChart()

    # Quit Pygame
    pygame.quit()
    sys.exit()
