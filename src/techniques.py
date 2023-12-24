"""Contains the various techniques humans would use to solve a sudoku puzzle"""
from board_driver import BoardDriver
from data import PencilMarks

def fill_pencil_marks(board_driver : BoardDriver):
    """Create pencilmarks for all missing digits in the puzzle"""
    SIZE = 10  # Constant for the size of the puzzle
    columns = [board_driver.get_col(i) for i in range(1, SIZE)]
    boxes = [board_driver.get_box(i) for i in range(1, SIZE)]
    board = board_driver.get_board_data()

    pencil_data = []
    for row, row_id in enumerate(board):
        row_of_pencil_marks = []
        for digit, col_id in enumerate(row):
            if digit == 0:
                row_of_pencil_marks.append(None)
                continue
            box_id = (row_id // 3) * 3 + (col_id // 3)

            pencil_mark = PencilMarks()
            for possible_digit in range(1, SIZE):
                conditions = (
                    possible_digit not in row,
                    possible_digit not in columns[col_id],
                    possible_digit not in boxes[box_id]
                )

                if all(conditions):
                    pencil_mark.add_digit(possible_digit)

            row_of_pencil_marks.append(pencil_mark)

        pencil_data.append(row_of_pencil_marks)
    return pencil_data

def single_position():
    """Single position in a row, col, or box that a digit could go"""
    return False

def single_candidate():
    """Single digit possible for a given box"""
    return False
