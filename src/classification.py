"""Utilize human solving techniques to give useful information
about sudoku boards
"""
import board_driver
import techniques
import data
def generate_difficulty(difficulty):
    """"Generates a puzzle of the given difficulty and returns it"""
    board = difficulty
    return board


def classify_difficulty(board):
    """Determines the difficulty of the provided puzzle"""
    driver = board_driver.BoardDriver(board)
    pencil_marks = techniques.fill_pencil_marks(driver)

    difficulty = 0
    while True:
        if techniques.single_position(pencil_marks, driver):
            difficulty += 100
            continue
        if techniques.single_candidate(pencil_marks, driver):
            difficulty += 100
            continue
        if driver.is_complete():
            print("puzzles is solved")
            break
        print("puzzle cannot be solved")
        break
    driver.print_board()
