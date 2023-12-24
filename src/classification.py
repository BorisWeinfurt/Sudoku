"""Utilize human solving techniques to give useful information
about sudoku boards
"""
import board_driver
import data
def generate_difficulty(difficulty):
    """"Generates a puzzle of the given difficulty and returns it"""
    board = difficulty
    return board


def classify_difficulty(board):
    """Determines the difficulty of the provided puzzle"""
    board_driver.BoardDriver(data.sudoku_puzzle_test)
    return board
