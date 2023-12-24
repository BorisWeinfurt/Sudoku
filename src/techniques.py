"""Contains the various techniques humans would use to solve a sudoku puzzle"""
from board_driver import BoardDriver
from data import Position
def single_position(driver):
    """Single position in a row, col, or box that a digit could go"""
    return False

def single_candidate(driver : BoardDriver):
    """Single digit possible for a given square"""
    for row_num, row in enumerate(driver.get_pencil_data().dump_pencil_data()):
        for col_num, pencil_mark in enumerate(row):
            if pencil_mark is not None:
                digits = pencil_mark.get_pencil_marks()
                if len(digits) == 1:
                    position = Position(row_num, col_num)
                    driver.add_digit(position, digits[0])
                    return True
    return False
