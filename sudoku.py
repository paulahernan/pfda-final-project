import random
import pygame
import sys 

pygame.init()
pygame.display.set_caption("Sudoku Puzzles")
resolution = (800,600)
screen = pygame.display.set_mode(resolution)
font = pygame.font.SysFont("arial", 40)
white = (255,255,255)
black = (0,0,0)
blue = (50,50,255)
gray = (200,200,200)
width = 500
height = 600
running = True 
fullscreen = None
cell_size = width // 9
selected = None



grid_easy1 = [
    [6,0,7,4,0,0,0,5,0],
    [0,3,0,0,0,1,0,2,8],
    [0,0,4,8,9,0,0,0,3],
    [0,0,0,0,5,6,2,3,9],
    [1,0,0,0,0,0,0,0,7],
    [3,5,9,2,4,0,0,0,0],
    [7,0,0,0,6,8,1,0,0],
    [5,9,0,7,0,0,0,8,0],
    [0,4,0,0,0,2,6,0,5]
]
grid_easy2 = [
    [3,1,0,0,0,0,0,0,9],
    [0,6,0,0,4,9,5,3,1],
    [4,0,9,0,0,3,7,6,0],
    [0,0,5,0,3,1,0,9,4],
    [8,0,2,0,7,6,3,0,0],
    [0,0,0,4,5,2,0,0,6],
    [0,0,0,0,8,0,1,0,0],
    [0,3,0,0,0,7,0,8,2],
    [0,0,1,0,9,4,0,0,0]
]
grid_easy3 = [
    [0,3,7,0,9,0,2,0,0],
    [6,0,0,0,7,8,5,3,9],
    [0,0,9,2,4,3,7,1,0],
    [0,0,0,0,3,9,8,0,1],
    [9,0,6,0,2,7,0,4,5],
    [4,8,0,0,5,0,0,7,0],
    [0,2,1,0,0,0,0,9,7],
    [0,9,0,7,0,0,0,0,0],
    [0,0,0,0,0,5,4,0,0]
]
grid_medium1 = [
    [0,0,7,3,0,1,9,0,0],
    [1,3,0,0,0,0,0,4,8],
    [9,0,0,0,6,0,0,0,5],
    [0,0,0,0,5,0,0,0,0],
    [2,0,3,0,0,0,8,0,9],
    [0,0,0,8,0,4,0,0,0],
    [0,0,0,6,0,3,0,0,0],
    [3,0,0,0,0,0,0,0,1],
    [8,0,0,7,1,9,0,0,3]
]
grid_medium2 = [
    [0,0,4,0,0,0,0,0,9],
    [8,0,0,0,6,0,0,5,3],
    [0,0,3,0,5,7,0,0,0],
    [4,6,0,2,0,0,0,0,0],
    [0,7,0,1,9,0,8,0,0],
    [0,9,0,0,7,0,0,6,0],
    [0,0,0,0,4,0,0,9,8],
    [0,0,0,0,2,0,4,3,6],
    [0,0,5,0,0,0,0,0,7]
]
grid_medium3 = [
    [3,6,0,0,0,7,0,0,4],
    [8,0,0,0,5,3,9,0,7],
    [0,9,2,0,0,8,0,6,0],
    [0,0,0,0,8,1,0,0,6],
    [0,0,0,0,7,6,0,3,0],
    [0,0,0,0,9,0,4,0,0],
    [0,0,0,0,6,0,1,5,0],
    [0,1,8,0,0,0,0,0,0],
    [4,0,0,2,0,0,0,0,9]
]
grid_hard1 = [
    [9,0,5,0,0,7,0,0,0],
    [0,3,0,0,2,8,0,7,0],
    [2,0,0,0,6,9,0,0,0],
    [1,0,0,0,0,0,0,5,0],
    [0,0,0,0,7,3,0,0,0],
    [0,8,0,1,0,0,4,0,3],
    [0,0,0,0,0,0,0,0,8],
    [0,0,0,9,0,0,0,6,5],
    [6,1,2,0,0,0,0,4,0]
]
grid_hard2 = [
    [9,1,0,6,0,5,0,0,0],
    [6,0,0,0,1,0,0,0,9],
    [0,0,0,0,0,8,2,0,0],
    [2,0,4,9,0,0,3,0,0],
    [5,0,0,0,0,7,0,6,0],
    [0,0,7,0,0,0,1,0,0],
    [0,3,0,5,0,0,6,0,0],
    [0,0,0,0,0,4,0,2,3],
    [8,0,0,0,0,0,0,0,0]
]
grid_hard3 = [
    [9,0,0,0,0,7,0,8,0],
    [0,0,1,0,5,0,0,7,0],
    [4,5,0,1,0,0,0,0,9],
    [0,0,0,0,3,0,9,0,0],
    [0,0,0,0,0,0,6,0,0],
    [0,0,0,0,9,2,5,0,0],
    [0,6,0,0,7,0,0,0,3],
    [2,0,9,0,8,0,0,5,0],
    [0,8,0,0,4,0,0,0,0]
]

#def current_grid():
    #grids_easy = [grid_easy1, grid_easy2, grid_easy3]
    #idx = random.randrange(3)
    #return grids_easy(idx)
#grids_medium = [grid_medium1, grid_medium2, grid_medium3]
#grids_hard = [grid_hard1, grid_hard2, grid_hard3]

def draw_grid():
    for i in range(10):
        if i % 3 == 0:
            thickness = 4
        else:
            thickness = 1
        pygame.draw.line(screen, black, (i* cell_size,0), (i*cell_size, width), thickness)
        pygame.draw.line(screen, black, (0,i*cell_size), (width, i * cell_size), thickness)
def draw_numbers():
        for row in range(9):
          for col in range(9):
                 number = grid_easy1[row][col]

                 if number != 0:
                    text = font.render(str(number), True, black)

                    x = col * cell_size + 18
                    y = row * cell_size + 10
                    screen.blit(text, (x,y))
def draw_selection():
     if selected:
          row,col = selected
          pygame.draw.rect(screen,blue,(col*cell_size,row*cell_size,cell_size,cell_size),4)
def valid(board,num,pos):
     row,col = pos

     for i in range(9):
          if board[row][i] == num and i != col:
               return False
     for i in range(9):
          if board[i][col] == num and i != row:
               return False 
     cell_y = row // 3
     cell_x = col // 3
     for i in range(cell_y*3,cell_y*3 +3):
          for j in range(cell_x*3, cell_x*3 +3):
               if board[i][j] == num and (i,j) != pos:
                    return False
     return True

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

        if event.type == pygame.KEYDOWN and selected:
            row, col = selected 
            if grid_easy1[row][col] == 0:
                 if event.key == pygame.K_1:
                      num = 1
                 elif event.key == pygame.K_2:
                      num = 2
                 elif event.key == pygame.K_3:
                      num = 3
                 elif event.key == pygame.K_4:
                      num = 4
                 elif event.key == pygame.K_5:
                      num = 5
                 elif event.key == pygame.K_6:
                      num = 6
                 elif event.key == pygame.K_7:
                      num = 7
                 elif event.key == pygame.K_8:
                      num = 8
                 elif event.key == pygame.K_9:
                      num = 9
                 else:
                      num = None
                 if num:
                      if valid(grid_easy1,num,(row,col)):
                           grid_easy1[row][col] = num

    screen.fill(white)
    draw_grid()
    draw_numbers()
    draw_selection()
    pygame.display.update()


pygame.quit()
sys.exit()

#if __name__=="__main__":
    #main()