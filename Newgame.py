def start_new_game():
    print("Starting a new game...")

    # Assuming '□' represents an empty space on the board
    empty_space = '□'

    # Create a 20x20 board with an outline of squares
    rows, cols = 22, 22
    game_board = [['□' if i == 0 or i == rows - 1 or j == 0 or j == cols - 1 else '-' for j in range(cols)] for i in range(rows)]

    # Print the board
    for row in game_board:
        print(' '.join(row))

    # Add your additional game initialization logic here


