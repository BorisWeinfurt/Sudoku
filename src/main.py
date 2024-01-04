"""
Main module runs the sudoku
User will be able to specify which functionality will be used
"""
import data
import board_driver
import classification


def main():
    """Main method creates a sudoku board and gives it to either the player or solver"""
    # Initialize the Sudoku board
    # driver = board_driver.BoardDriver(data.sudoku_puzzle_test)
    # Puzzle classification
    puzzles = data.sudoku_puzzle_test
    for puzzle_num, puzzle in enumerate(puzzles):
        print("Puzzle num", puzzle_num)
        classification.classify_difficulty(puzzle)
    # classification.classify_difficulty(puzzles[7])

    # Play the game
    # player_play_game(driver)

def player_play_game(driver):
    """User interactive terminal based sudoku game"""
    print("Welcome to Sudoku!")

    while not driver.is_complete():
        # Display the current state of the board
        driver.print_board()
        print()

        # Get user input for row, column, and digit
        row = int(input("Enter the row (1-9): ")) - 1
        col = int(input("Enter the column (1-9): ")) - 1
        digit = int(input("Enter the digit (1-9): "))

        # Validate and add the player's guess
        position = data.Position(row, col)
        if driver.add_digit(position, digit):
            print("Your guess is correct!\n")
        else:
            print("Invalid guess. Try again.\n")

    print("Congratulations! You've completed the Sudoku puzzle.")

if __name__ == "__main__":
    main()
