def set_up():
    '''
    set_up() -> list
    sets up the connect four players
    '''
    p1 = str(input("Player X's name is:  "))
    p2 = str(input("Player O's name is:  "))
    p1 = p1.strip()
    p2 = p2.strip()
    while p1 == '':
        p1 = str(input("Player X's name is:  "))
    while p2 == '':
        p2 = str(input("Player X's name is:  "))
    while p1 == p2:
        p1 = str(input("Player X's name is:  "))
        p2 = str(input("Player O's name is:  "))
    return [p1,p2]
players = set_up()
p1 = players[0]
p2 = players[1]
n_rows = 6
n_columns = 7
n_inaline = 4       # 4 because you need to connect 4 in a line to win
grid = []
for i in range(n_rows):
    grid.append(['.']*n_columns)
def gravity(grid):
    '''
    gravity(list) -> list
    This function enacts gravity 
    but only brings O's or X's in the air down by one,
    not down the whole column.
    '''
    new_grid = []
    for i in range(n_rows):
        new_grid.append(['.']*n_columns)
    for row in range(n_rows):   
        for column in range(n_columns):
            if grid[row][column]!=".":
                if row == n_rows-1:
                    new_grid[row][column] = grid[row][column]
                elif grid[row+1][column]==".":
                    new_grid[row][column] = "."
                    new_grid[row+1][column] = grid[row][column]
                else:
                    new_grid[row][column] = grid[row][column]                    
    return new_grid
def win(grid):
    '''
    This function takes in 
    win(list) -> 'X' or 'O' or ''
    The function tells you whether or not someone has won
    and who won.
    '''
    # check if anybody won horizantaly
    for row in range(n_rows):
        for column in range(n_columns-n_inaline+1):
            equal = 0
            for place in range(n_inaline):
                if grid[row][column] !='.':
                    if grid[row][column]==grid[row][column+place]:
                        equal += 1
            if equal == n_inaline:
                return grid[row][column]
    # check if anybody won verticaly
    for row in range(n_rows-n_inaline+1):
        for column in range(n_columns):
            equal = 0
            for place in range(n_inaline):
                if grid[row][column] !='.':
                    if grid[row][column]==grid[row+place][column]:
                        equal += 1
            if equal == n_inaline:
                return grid[row][column]
    # diagonal one way
    for row in range(n_rows-n_inaline+1):
        for column in range(n_columns-n_inaline+1):
            equal = 0
            for place in range(n_inaline):
                if grid[row][column] != '.':
                    if grid[row][column] == grid[row+place][column+place]:
                        equal += 1
            if equal == n_inaline:
                return grid[row][column]
    # diagonal the other way
    for row in range(3):
        for column in range(n_columns-n_inaline,n_columns):
            equal = 0
            for place in range(n_inaline):
                if grid[row][column] != '.':
                    if grid[row][column] == grid[row+place][column-place]:
                        equal += 1
            if equal == n_inaline:
                return grid[row][column]
    return ' '
# The below is the actual game code, not the functions
player_turn = 0
while win(grid) == ' ':
    print("1 2 3 4 5 6 7")
    for row in range(6):
        line = ''
        for column in range(7):
            line += grid[row][column]+' '
        print(line)
    if player_turn%2 == 0:
        X_word = int(input((p1+" You're X, what column do you want to play in(enter in a number, or else...)?  ")))
        while grid[0][X_word-1] != '.':
            X_word = int(input(("Please choose a different column. What column do you want to play, "+p1+"?  ")))
        grid[0][X_word-1] = "X"
        grid = gravity(gravity(gravity(gravity(gravity(grid)))))
    else:
        O_word = int(input((p2+" You're O, what column do you want to play in(enter in a number, or else...)?  "  )))
        while grid[0][O_word-1] != '.':
            O_word = int(input(("Please choose a different column. What column do you want to play, "+p2+"?  "  )))
        grid[0][O_word-1] = "O"
        grid = gravity(gravity(gravity(gravity(gravity(grid)))))
    player_turn += 1
print("1 2 3 4 5 6 7")
for row in range(6):
    line = ''
    for column in range(7):
        line += grid[row][column]+' '
    print(line)
if win(grid) == 'X':
    print("Congratulations "+p1+", you won!")
if win(grid) == 'O':
    print("Congratulations "+p2+", you won!")


    
