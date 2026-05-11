import random
import pygame
import sys 

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
class Buttons():
    def __init__(self, pos, width, height,text_input, font, base_color, hovering_color):

        self.x_pos = pos[0]
        self.y_pos = pos[1]

        self.width = width
        self.height = height

        self.font = font
        self.base_color = base_color
        self.hovering_color = hovering_color
        self.text_input = text_input
        self.current_color = self.base_color

        self.rect = pygame.Rect(self.x_pos - width // 2,self.y_pos - height // 2,width,height)

        self.text = self.font.render(self.text_input, True, (0, 0, 0))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    # ORIGINAL METHOD
    def update(self, screen):
        pygame.draw.rect(screen, self.current_color,
                         self.rect, border_radius=12)
        screen.blit(self.text, self.text_rect)

    # ORIGINAL CLICK CHECK
    def Input(self, position):
        return self.rect.collidepoint(position)

    # ORIGINAL HOVER LOGIC
    def change_color(self, position):
        if self.rect.collidepoint(position):
            self.current_color = self.hovering_color
        else:
            self.current_color = self.base_color

    # ---- MINIMAL COMPATIBILITY (NOT CHANGING ORIGINAL STYLE) ----
    def draw(self, screen):
        self.update(screen)

    def check_hover(self, position):
        self.change_color(position)

    def clicked(self, position):
        return self.Input(position)
    
class Sudoku():
    def __init__(self):
        self.resolution = (800,600)
        self.screen = pygame.display.set_mode(self.resolution)
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.blue = (50,50,255)
        self.gray = (200,200,200)
        self.green = (0,250,0)
        self.width = 500
        self.cell_size = self.width // 9
        self.display = "menu"
        self.selected = None
        self.current_grid = None
        self.editable_grid = None
        self.title_font = pygame.font.SysFont("arial", 70)
        self.font = pygame.font.SysFont("arial", 40)
        center = self.resolution[0] // 2
        self.easy = Buttons((center, 200), 250, 70, "EASY", self.font, self.gray, self.green)
        self.medium = Buttons((center,320),250,70, "MEDIUM", self.font, self.gray,self.green)
        self.hard = Buttons((center,440), 250,70, "HARD", self.font, self.gray, self.green)
        self.back = Buttons((center,550),250,70,"BACK", self.font, self.gray, self.green)

    def get_grid(self,level):
        if level == "easy":
            grids_easy = [grid_easy1, grid_easy2, grid_easy3]
            idx = random.randrange(3) 
            current_grid = grids_easy[idx]
        elif level == "medium":
            grids_medium = [grid_medium1, grid_medium2, grid_medium3]
            idx = random.randrange(3)
            current_grid = grids_medium[idx]
        elif level == "hard":
            grids_hard = [grid_hard1, grid_hard2, grid_hard3]
            idx = random.randrange(3)
            current_grid = grids_hard[idx]
        return current_grid, [row[:] for row in current_grid]
        
    def play(self):
       self.screen.fill(self.white)
       if self.display == "menu":
           title = self.title_font.render("SUDOKU", True, self.blue)
           title_rect = title.get_rect(center=(self.resolution[0]//2,80))
           self.screen.blit(title,title_rect)
           for buttons in [self.easy,self.medium,self.hard]:
               buttons.draw(self.screen)
       elif self.display == "game":
            self.draw_grid()
            self.draw_numbers()
            self.draw_selection()
            self.back.draw(self.screen)

    def draw_grid(self):
        for i in range(10):
            if i % 3 == 0:
                thickness = 4
            else:
                thickness = 1
        
            pygame.draw.line(
                self.screen, 
                self.black, 
                (i* self.cell_size,0), 
                (i*self.cell_size, self.width),
                thickness
            )
            pygame.draw.line(
                self.screen, 
                self.black, 
                (0,i*self.cell_size), 
                (self.width, i * self.cell_size),
                thickness
            )

    def draw_numbers(self):
        for row in range(9):
            for col in range(9):
                number = self.editable_grid[row][col]

                if number != 0:
                    text = self.font.render(str(number), True, self.black)

                    x = col * self.cell_size + 18
                    y = row * self.cell_size + 10
                    self.screen.blit(text, (x,y))
    def draw_selection(self):
     if self.selected:
          row,col = self.selected
          pygame.draw.rect(self.screen,self.blue,(col*self.cell_size,row*self.cell_size,self.cell_size,self.cell_size),4)
    def valid(self,board,num,pos):
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



def main():
    pygame.init()
    pygame.display.set_caption("Sudoku Puzzles")
    game = Sudoku()

    running = True  
    while running:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if game.display == "menu":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if game.easy.clicked(mouse):
                        game.current_grid,game.editable_grid = game.get_grid("easy")
                        game.display = "game"
                    elif game.medium.clicked(mouse):
                        game.current_grid, game.editable_grid = game.get_grid("medium")
                        game.display = "game"
                    elif game.hard.clicked(mouse):
                        game.current_grid, game.editable_grid = game.get_grid("hard")
                        game.display = "game"
            elif game.display == "game":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
                    if x < game.width and y < game.width:
                        col = x // game.cell_size
                        row = y // game.cell_size
                        game.selected = (row,col)
                    elif game.back.clicked(mouse):
                        game.display = "menu"

            if event.type == pygame.KEYDOWN and game.selected:
                row, col = game.selected 
                num = None
                if game.current_grid[row][col] == 0:
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
                    elif event.key == pygame.K_BACKSPACE:
                      game.editable_grid[row][col] = 0
                    if num:
                      if game.valid(game.editable_grid,num,(row,col)):
                           game.editable_grid[row][col] = num
        for buttons in [game.easy, game.medium, game.hard]:
            buttons.check_hover(mouse)
        if game.display == "game":
            game.back.check_hover(mouse)

        game.play()
        pygame.display.update()
    pygame.quit()
    sys.exit()

if __name__=="__main__":
    main()