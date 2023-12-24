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
    driver = board_driver.BoardDriver(data.sudoku_puzzle_test)
    pencil_marks = techniques.fill_pencil_marks(board)

    difficulty = 0
    while True:
        if techniques.single_position():
            difficulty += 100
        elif techniques.single_candidate():
            difficulty += 100
        break
    return board
