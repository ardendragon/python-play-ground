def get_players():
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
        p2 = str(input("Player O's name is:  "))
    while p1 == p2:
        p1 = str(input("Player X's name is:  "))
        p2 = str(input("Player O's name is:  "))
    return [p1, p2]


def gravity(grid):
    '''
    gravity(list) -> list
    This function enacts gravity 
    but only brings O's or X's in the air down by one,
    not down the whole column.
    '''
    n_rows = len(grid)
    n_columns = len(grid[0])
    new_grid = []
    for i in range(n_rows):
        new_grid.append(['.']*n_columns)
    for row in range(n_rows):
        for column in range(n_columns):
            if grid[row][column] != ".":
                if row == n_rows-1:
                    new_grid[row][column] = grid[row][column]
                elif grid[row+1][column] == ".":
                    new_grid[row][column] = "."
                    new_grid[row+1][column] = grid[row][column]
                else:
                    new_grid[row][column] = grid[row][column]
    return new_grid


def identify_winner(grid, connect_n):
    '''
    This function takes in 
    win(list, int) -> 'X' or 'O' or ''
    The function tells you whether or not someone has won
    and who won.
    '''
    # check if anybody won horizantaly
    for row in range(n_rows):
        for column in range(n_columns-connect_n+1):
            equal = 0
            for place in range(connect_n):
                if grid[row][column] != '.':
                    if grid[row][column] == grid[row][column+place]:
                        equal += 1
            if equal == connect_n:
                return grid[row][column]
    # check if anybody won verticaly
    for row in range(n_rows-connect_n+1):
        for column in range(n_columns):
            equal = 0
            for place in range(connect_n):
                if grid[row][column] != '.':
                    if grid[row][column] == grid[row+place][column]:
                        equal += 1
            if equal == connect_n:
                return grid[row][column]
    # diagonal one way
    for row in range(n_rows-connect_n+1):
        for column in range(n_columns-connect_n+1):
            equal = 0
            for place in range(connect_n):
                if grid[row][column] != '.':
                    if grid[row][column] == grid[row+place][column+place]:
                        equal += 1
            if equal == connect_n:
                return grid[row][column]
    # diagonal the other way
    for row in range(n_rows-connect_n+1):
        for column in range(n_columns-connect_n, n_columns):
            equal = 0
            for place in range(connect_n):
                if grid[row][column] != '.':
                    if grid[row][column] == grid[row+place][column-place]:
                        equal += 1
            if equal == connect_n:
                return grid[row][column]
    return ''


def get_valid_placement(input_str, columns, player, grid):
    '''
    get_valid(str) -> int
    This function makes sure the output will be a valid column to place in.
    '''
    is_not_digit = True
    word = input_str
    while is_not_digit:
        if word.isdigit() == True:
            col = int(word)
            if col <= columns and col >= 1 and grid[0][col-1] == '.':
                is_not_digit = False
            else:
                word = input(
                    "Please input a number within the range. What column do you want to play, "+player+"?  ")
        else:
            word = input(
                "Please input a number within the range. What column do you want to play, "+player+"?  ")
    return int(word)


def draw_grid(grid):
    '''
    draw_grid(int,int,list) -> None
    draws the grid with rows and columns
    '''
    line = ''
    rows = len(grid)
    columns = len(grid[0])
    for column in range(columns):
        line += str(column+1)+' '
    print(line)
    for row in range(rows):
        line = ''
        for column in range(columns):
            line += grid[row][column]+' '
        print(line)


if __name__ == "__main__":
    # set up variables
    players = get_players()
    p1 = players[0]
    p2 = players[1]
    n_rows = 6
    n_columns = 7
    total_turns = n_rows*n_columns
    # 4 because you need to connect 4 in a line to win
    n_connect = 4
    grid = []
    # initialize the grid
    for i in range(n_rows):
        grid.append(['.']*n_columns)

    player_turn = 0
    winner = identify_winner(grid, n_connect)
    while not winner and player_turn < total_turns:
        print(player_turn)
        # draws the grid
        draw_grid(grid)
        # if it's X's turn
        if player_turn % 2 == 0:
            X_col = input(
                p1+" You're X, what column do you want to play in?  ")
            X_col = get_valid_placement(X_col, n_columns, p1, grid)
            grid[0][X_col-1] = "X"
        # if it's O's turn
        else:
            O_col = input(
                p2+" You're O, what column do you want to play in?  ")
            O_col = get_valid_placement(O_col, n_columns, p2, grid)
            grid[0][O_col-1] = "O"

        # updates the grid
        for i in range(n_columns-1):
            grid = gravity(grid)
        player_turn += 1
        winner = identify_winner(grid, n_connect)

    draw_grid(grid)

    # who wins??????
    if winner == 'X':
        print("Congratulations "+p1+", you won!")
    elif winner == 'O':
        print("Congratulations "+p2+", you won!")
    else:
        print("It's a draw! Good game :)")
