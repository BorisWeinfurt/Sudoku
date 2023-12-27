"""Contains the various techniques humans would use to solve a sudoku puzzle"""
from board_driver import BoardDriver
from data import Position
def single_position(driver : BoardDriver):
    """Single position in a row, col, or box that a digit could go"""
    size = 9
    pencil_data = driver.get_pencil_data()
    for i in range(0,9):
        # Do rows -----------
        pencil_row = pencil_data.get_row(i)
        digit_row = driver.get_row(i)

        for digit in range(1,10):
            if digit in digit_row:
                continue

            possible_location = -1
            for col_index, pencil_mark in enumerate(pencil_row):
                if pencil_mark is not None and digit in pencil_mark.get_pencil_marks():
                    if possible_location == -1:
                        possible_location = col_index
                    else:
                        possible_location = -1
                        break
            # exiting the loop without -1 means a single possible location has been found
            if possible_location != -1:
                position = Position(i, possible_location)
                driver.add_digit(position, digit)
                return True

        # Do colums -----------
        pencil_col = pencil_data.get_col(i)
        digit_col = driver.get_col(i)

        for digit in range(1,10):
            if digit in digit_col:
                continue

            possible_location = -1
            for col_index, pencil_mark in enumerate(pencil_col):
                if pencil_mark is not None and digit in pencil_mark.get_pencil_marks():
                    if possible_location == -1:
                        possible_location = col_index
                    else:
                        possible_location = -1
                        break
            # exiting the loop without -1 means a single possible location has been found
            if possible_location != -1:
                position = Position(possible_location, i)
                driver.add_digit(position, digit)
                return True
        # Do boxes
        pencil_box = pencil_data.get_box(i)
        digit_box = driver.get_box(i)

        for digit in range(1,10):
            if digit in digit_box:
                continue

            possible_location = -1
            for box_index, pencil_mark in enumerate(pencil_box):
                if pencil_mark is not None and digit in pencil_mark.get_pencil_marks():
                    if possible_location == -1:
                        possible_location = box_index
                    else:
                        possible_location = -1
                        break
            # exiting the loop without -1 means a single possible location has been found
            if possible_location != -1:
                init_row = i // 3 * 3
                init_col = i % 3 * 3
                row_offset = possible_location // 3
                col_offset = possible_location % 3
                position = Position(init_row + row_offset, init_col + col_offset)
                driver.add_digit(position, digit)
                return True
    return False

def single_candidate(driver : BoardDriver):
    """Single digit possible for a given square"""
    # print("entering single cndaidate")
    for row_num, row in enumerate(driver.get_pencil_data().dump_pencil_data()):
        for col_num, pencil_mark in enumerate(row):
            if pencil_mark is not None:
                digits = pencil_mark.get_pencil_marks()
                if len(digits) == 1:
                    position = Position(row_num, col_num)
                    driver.add_digit(position, digits[0])
                    return True
    return False
