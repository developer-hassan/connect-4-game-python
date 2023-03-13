# Import random module for generating random numbers
import random

# Defining the number of rows and columns by using global constants
NUM_ROWS = 6
NUM_COLS = 7


def validate_players(players):
    """
    Validates the number of players playing entered by the user.

    Args:
    - players (int): integer number of players entered by the user

    Returns:
    - True if the players are between 2 and 5 (both inclusive) otherwise False.
    """
    return players >= 2 and players <= 5


def get_valid_players():
    """
    Get the valid number of players from the user. It keeps on taking the input from the user until the right right input is entered

    Returns:
    - The number of valid players entered by the user.
    """
    valid_players = False
    # Run the loop until the right player numbers is entered
    while not valid_players:
        # Get the number of players from user
        num_players = int(input("Enter the number of players playing: "))
        # Validate the players to check whether they are in right range
        valid_players = validate_players(num_players)

        # Display message according to players entered
        if valid_players:
            print("Players Saved Successfully!")
        else:
            print("Invalid Players Entered!")
    return num_players


def assign_checkers(players):
    """
    Assign a checker character to each player and stores in a Python dictionary.

    Args:
    - players (int): integer number of (valid) players entered by the user

    Returns:
    - True if the players are between 2 and 5 (both inclusive) otherwise False.
    """
    # List of checkers for each player
    checkers = ["#", "O", "X", "Q", "*"]

    # Store players and their checkers in a dictionary
    players_and_checkers = {}

    for i in range(players):
        players_and_checkers[i] = checkers[i]

    return players_and_checkers


def initialize_board():
    """
    Initialize the board with empty strings in each cell

    Returns
    - A 2D array with spaces as each index in each row.
    """
    board = []

    # Initialize the board with space characters to be stored initially
    for row in range(NUM_ROWS):
        row_elements = []
        for col in range(NUM_COLS):
            row_elements.append(' ')
        board.append(row_elements)
    return board


def print_board(board):
    """
    Display the board's cell values.

    Args:
    - A game board (2D-Array) which is to be printed.
    """

    # Print the column names and board values
    for cols in range(NUM_COLS):
        print('  ' + chr(cols+65), end=' ')
    print("\n+" + "---+" * NUM_COLS)

    for row in range(NUM_ROWS):
        print('|', end=' ')
        for col in range(NUM_COLS):
            print(board[row][col] + ' | ', end="")
        print("\n+"+"---+"*NUM_COLS)


def validate_column(user_input):
    """
    Returns true if user input is valid otherwise returns false.

    Args:
    - user_input (int): A column index to check whether it is in a given range

    Returns:
    - True if the input is in valid range. Otherwise returns False. 
    """
    return user_input in range(NUM_COLS)


def get_valid_column(turn):
    """
    Get the valid column input from the user. It keeps on taking input from user until the right value is entered.

    Args:
    - turn (int): A current player who is playing to get input from them.

    Returns:
    - Returns the valid column number inputted by the user.
    """
    valid_column = False

    # Gets the column information from the user until the right column is entered
    while not valid_column:
        # Input the column number from user
        column = input(f"Player {turn}, please enter a column (e.g. A): ")
        # Store the column number index
        column = ord(column) - ord("A")
        # Validate column
        valid_column = validate_column(column)
        if not valid_column:
            print("Invalid Column Name Entered!")
    return column


def place_checker(board, column, checker):
    """
    It places the player's checker on the board.

    Args:
    - board (2D-Array): A board (2D-Array) on which we are going to place the checker.
    - column (int): An index of column on which the checker will be placed.
    - checker (string): A character value which will be placed as a checker on the board.

    Returns:
    - True if the checker is placed correctly. Otherwise returns False.
    """
    checker_is_placed = False
    for row in range(NUM_ROWS - 1, -1, -1):
        for col in range(NUM_COLS):
            if col == column:
                if board[row][col] != " ":
                    continue
                else:
                    board[row][col] = checker
                    checker_is_placed = True
                    break
        if checker_is_placed:
            break

    return checker_is_placed


def check_game_end(board, checker):
    """
    Check the end of game after each move. First check for the draw state (all cells filled). Then checks for player win.
    It checks if the player is win with its horizontal, vertical, or diagonal connection of checkers.

    Args:
    - board (2D-Array): A 2D-Array game board on which the checkers comparison will be made
    """

    # If there is no " " in board, the game is draw
    is_draw = True
    # For each list inside a 2D-list
    for row in board:
        # If any empty space is present in a list
        if " " in row:
            # It means the game is not draw yet
            is_draw = False
            # No need to check further
            break

    # If the game is draw, no need to check the win and returns draw
    if is_draw:
        return "Draw"

    # Initially no checkers connection is found
    found = False
    # For each column in each row of the board
    for row in range(NUM_ROWS):
        # for each column in board
        for col in range(NUM_COLS):
            # Check for the cell whose value match with the player's checker
            if board[row][col] == checker:
                # Horizontal logic - row remains the same
                if col <= NUM_COLS - 4:
                    # If four checkers are placed in a row adjacently
                    if board[row][col+1] == board[row][col+2] == board[row][col+3] == board[row][col]:
                        # It means the current player is won and no need to check further
                        found = True
                        break

                # Vertical logic - column remains the same
                if row <= NUM_ROWS - 4:
                    # If four checkers are placed in a column adjacently
                    if board[row+1][col] == board[row+2][col] == board[row+3][col] == board[row][col]:
                        # It means the current player is won and no need to check further
                        found = True
                        break

                # Anti-diagonal logic - columns of left side are checked
                if col > 2 and row <= NUM_ROWS - 4:
                    # If four checkers are placed in a left diagonal adjacently
                    if board[row+1][col-1] == board[row+2][col-2] == board[row+3][col-3] == board[row][col]:
                        # It means the current player is won and no need to check further
                        found = True
                        break

                # Diagonal logic - columns of right side are checked
                if col < 4 and row <= NUM_ROWS - 4:
                    # If four checkers are placed in a right diagonal adjacently
                    if board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3] == board[row][col]:
                        # It means the current player is won and no need to check further
                        found = True
                        break

        # Do not go ahead if the checkers are found in current row/column/diagonal
        if found:
            break

    return found


# Here the game begins
if __name__ == "__main__":

    # store the number of players by calling a function
    num_players = get_valid_players()
    # Store the players with their checkers
    players = assign_checkers(num_players)
    # Make an initial game board
    game_board = initialize_board()

    # Random turn
    turn = random.randint(0, num_players - 1)

    # Run the game until it is finished
    while True:
        # Print the board on console
        print_board(game_board)
        # Get the right column from the user
        user_column = get_valid_column(turn)
        # Place the player's checker on the column entered by the user
        checker_placed = place_checker(board=game_board,
                                       column=user_column,
                                       checker=players[turn])

        # If all checkers are already in a column, the turn will be lost
        if not checker_placed:
            print("Invalid Column Selected! All cells filled. Turn Lost :(")

        # Get the game result. Either a player wons or it is a draw
        game_result = check_game_end(game_board, players[turn])

        # If a game is draw then display that the game is draw
        if game_result == "Draw":
            print_board(game_board)
            print(f"Game is Draw!")
            break

        # If some player wins then display that player is win
        elif game_result:
            print_board(game_board)
            print(f"Player {turn} Won!")
            break

        # Change the turn of players
        turn = (turn + 1) % num_players
