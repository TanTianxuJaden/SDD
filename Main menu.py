from Newgame import start_new_game

class CityBuildingGame:
    def __init__(self):
        self.high_scores = []  # Placeholder for high scores
        self.current_game_state = None  # Placeholder for the current game state

    def display_main_menu(self):
        print("===== City Building Game =====")
        print("1. Start New Game")
        print("2. Load Saved Game")
        print("3. Display High Scores")
        print("4. Exit Game")

    def load_saved_game(self):
        print("Loading saved game...")
        # Your game loading logic goes here

    def display_high_scores(self):
        print("High Scores:")
        for i, score_entry in enumerate(self.high_scores, 1):
            print(f"{i}. {score_entry['name']}: {score_entry['score']} points")

    def exit_game(self):
        print("Exiting the game. Goodbye!")
        exit()

    def run(self):
        self.display_main_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            start_new_game()  # Call the function from Newgame.py
        elif choice == '2':
            self.load_saved_game()
        elif choice == '3':
            self.display_high_scores()
        elif choice == '4':
            self.exit_game()
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

# Example usage
if __name__ == "__main__":
    game = CityBuildingGame()
    game.run()