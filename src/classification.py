"""Utilize human solving techniques to give useful information
about sudoku boards
"""
import board_driver
import techniques

def generate_difficulty(difficulty):
    """"Generates a puzzle of the given difficulty and returns it"""
    board = difficulty
    return board


def classify_difficulty(board):
    """Determines the difficulty of the provided puzzle"""
    driver = board_driver.BoardDriver(board)

    difficulty = 0
    while True:
        if techniques.single_position(driver):
            print("single position success")
            difficulty += 100
            continue
        if techniques.single_candidate(driver):
            print("single candidate success")
            difficulty += 100
            continue
        if techniques.pointing_pairs_and_triples(driver):
            print("pointing candidates success")
            difficulty += 100
            continue
        if driver.is_complete():
            print("Puzzle is solved!")
            break
        print("puzzle cannot be solved")
        break
    driver.print_board()
