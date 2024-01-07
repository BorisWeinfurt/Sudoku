"""
Main module runs the sudoku
User will be able to specify which functionality will be used
"""
import board_driver
import classification
from pprint import pprint
from data import Position


def main():
    """Main method creates a sudoku board and gives it to either the player or solver"""
    # Puzzle classification
    
    print("Welcome to the sudoku generator")
    print("Would you like to generate (gen), or play (play)")
    use_type = input()
    if use_type not in ["gen", "play"]:
        print("Invalid input")
        return
    
    print("Enter a difficulty: (e)asy, (m)edium, (h)ard, (t)ricky, (f)iendish")
    diff = input()
    
    if diff in ["e", "m", "h", "t","f"]:
            difficulty_mapping = {"e": 0, "m": 1, "h": 2, "t": 3, "f":4}
            difficulty_index = difficulty_mapping[diff]

    
    board = classification.generate_difficulty(difficulty_index)
    
    if use_type == "gen":
        print("Your board is:")
        pprint(board)
    elif use_type == "play":
        driver = board_driver.BoardDriver(board)
        player_play_game(driver)

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
        position = Position(row, col)
        if driver.add_digit(position, digit):
            print("Your guess is correct!\n")
        else:
            print("Invalid guess. Try again.\n")

    print("Congratulations! You've completed the Sudoku puzzle.")

if __name__ == "__main__":
    main()
