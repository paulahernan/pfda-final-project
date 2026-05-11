# Sudoku Puzzle

 ## Repository 
 https://github.com/paulahernan/pfda-final-project.git 

 ## Video 
 https://youtu.be/k2rheeDikyo

 ## Description 
    This project is a simple Sudoku game in which the player can solve up to 9 sudoku puzzles while giving them the liberty of choosing their own difficulty- 3 puzzles per level.
    
    The program opens at a main menu showcasing "SUDOKU" as the title while displaying three interactable buttons that read "EASY","MEDIUM", and "HARD" which lead the player to different levels of sudoku puzzles. When one of the buttons is pressed, the program randomly chooses one puzzle out of three to showcase for each difficulty. The screen/display then displays the sudoku puzzle which is interactable; if a cell from the board is clicked, the cell will be highlighted in blue to indicate it is selected and with player input- the player can select the corresponding number for the puzzle. If the player makes a mistake, the program allows for a number to be deleted by clicking backspace. The program also gives the player a handy "back" button which leads them back to the main menu. In case the program needs to be closed, it allows this by clicking the x button on top of the window display. 

    If I would to improve this project, I would've liked to center the display of the sudoku puzzles to make it look a little neater since in the program it is displayed more-so to the left side of the screen. I was having trouble figuring out how to center things with pygame.draw and the screen resolution I chose. I would also like to improve the validity system to inform the player more visually if they completed the puzzles successfuly through a win screen or through indications that there might have inserted numbers which are wrong. In the latter case, I think my skills aren't developed enough to figure out how I would encorporate that. 

 ## Sudoku Puzzle code sources/references:
 - https://www.geeksforgeeks.org/python/building-and-visualizing-sudoku-game-using-pygame/
 - https://medium.com/@ishitanegi09/building-a-sudoku-game-in-python-using-backtracking-8d218ea84e1b
 - https://github.com/PiyushG14/Pygame-sudoku/blob/main/sudoku.py
 - https://stackoverflow.com/questions/45471152/how-to-create-a-sudoku-puzzle-in-python

 ## Previous labs/chapter notes that really helped me
 - Digital rain lab (Pygame, class, methods, event loops)
 - Rock, Paper, Scissors lab (conditional statments to get specific results)
 - pattern quilt generator lab (Operators and grids)
 - magic sorting hat lab (Random library)

 ## Main Menu code sources/references:
 - https://github.com/baraltech/Menu-System-PyGame/tree/main/assets
 - https://programmingpixels.com/handling-a-title-screen-game-flow-and-buttons-in-pygame.html