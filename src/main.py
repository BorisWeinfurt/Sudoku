import data
import boardDriver

def main():
    # Initialize the Sudoku board
    driver = boardDriver.BoardDriver()

    # Play the game
    player_play_game(driver)

def player_play_game(driver):
    print("Welcome to Sudoku!")

    while not driver.isComplete():
        # Display the current state of the board
        driver.printBoard()
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
