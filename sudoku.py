import random
import pygame

def main():
    pygame.init()
    pygame.display.set_caption("Sudoku Puzzles")
    Clock = pygame.time.Clock()
    dt = 0 
    resolution = (800,600)
    screen = pygame.display.set_mode(resolution)
    x = 0 
    y = 0
    diff = 500/9
    val = 0 
     
    grid = [
        [6,0,7,4,0,0,0,5,0],
        [0,3,0,0,0,1,0,2,8],
        [0,0,4,8,9,0,0,0,3],
        [0,0,0,0,5,6,2,3,9],
        [1,0,0,0,0,0,0,0,7],
        [3,5,9,2,4,0,0,0,0],
        [7,0,0,0,6,8,1,0,0],
        [5,9,0,7,0,0,0,8,0],
        [0,4,0,0,0,2,6,0,5],
    ]

    running = True 
    fullscreen = None 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode(resolution)

    white = pygame.Color(255,255,255)
    screen.fill(white)
    dt = Clock.tick(12)
    pygame.quit()

if __name__=="__main__":
    main()