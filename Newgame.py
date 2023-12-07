def start_new_game():
    print("Starting a new game...")

    # Create a 22x22 board with labels
    rows, cols = 22, 22
    game_board = [
        [' ' if i == 0 or j == 0 else chr(64 + i) if j == 1 else str(j - 1) if i == 1 else '-' for j in range(cols)]
        for i in range(rows)
    ]

    # Print the board
    for row in game_board:
        print(' '.join(row))

    # Add your additional game initialization logic here

# Test the function
start_new_game()
