import random
import pygame

def main():
    pygame.init()
    pygame.display.set_caption("Sudoku Puzzles")
    Clock = pygame.time.Clock()
    dt = 0 
    resolution = (800,600)
    screen = pygame.display.set_mode(resolution)

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