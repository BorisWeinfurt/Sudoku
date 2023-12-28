"""Contains the various techniques humans would use to solve a sudoku puzzle"""
from board_driver import BoardDriver
from data import Position
import utils

def single_position(driver : BoardDriver):
    """Single position in a row, col, or box that a digit could go"""
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
    for row_num, row in enumerate(driver.get_pencil_data().dump_pencil_data()):
        for col_num, pencil_mark in enumerate(row):
            if pencil_mark is not None:
                digits = pencil_mark.get_pencil_marks()
                if len(digits) == 1:
                    position = Position(row_num, col_num)
                    driver.add_digit(position, digits[0])
                    return True
    return False

def pointing_pairs_and_triples(driver : BoardDriver):
    """Uses pointing pairs and/or triples to eliminate candidates"""
    for box_to_examine in range(0,9):
        box_digits = driver.get_box(box_to_examine)
        pencil_digits = driver.get_pencil_data().get_box(box_to_examine)
        for digit in range(1,10):
            if digit in box_digits:
                continue
            columns_impossible = False
            # rows
            for box_row_num in range(0,3):
                pencil_row = utils.get_row(pencil_digits, box_row_num)
                num_digit = utils.count_in_pencilmarks(pencil_row, digit)
                if num_digit == 1:
                    # if there is a single pencil mark
                    # AND its not a single position then it cant be a pointing row
                    # BUT it can still be a pointing column
                    break
                if num_digit >= 2:
                    # if there is a pointing row check that there are no other entries in the box
                    for clear_rows in range(box_row_num+1, 3):
                        pencil_row = utils.get_row(pencil_digits, clear_rows)
                        num_digit = utils.count_in_pencilmarks(pencil_row, digit)

                        if num_digit != 0:
                            columns_impossible = True
                            break

                    if columns_impossible:
                        break

                    # attempt to eliminate candidates using this pair
                    # if some were eliminated technique is a success
                    row_num = box_to_examine // 3 * 3 + box_row_num
                    if utils.pointing_row_eliminate(box_to_examine, driver.get_pencil_data().get_row(row_num), digit):
                        return True
            if columns_impossible: # if there cannot be a pointing column skip to the next digit
                continue
            # columns
            for box_col_num in range(0,3):
                pencil_col = utils.get_col(pencil_digits, box_col_num)
                num_digit = utils.count_in_pencilmarks(pencil_col, digit)
                if num_digit == 1:
                    # if there is a single pencil mark
                    # AND its not a single position then it cant be a pointing column
                    break
                if num_digit >= 2:
                    # if there is a pointing column check that there are no other entries in the box
                    for clear_cols in range(box_col_num+1, 3):
                        pencil_col = utils.get_col(pencil_digits, clear_cols)
                        num_digit = utils.count_in_pencilmarks(pencil_col, digit)

                        if num_digit != 0:
                            columns_impossible = True
                            break

                    if columns_impossible:
                        break

                    # attempt to eliminate candidates using this pair
                    # if some were eliminated technique is a success
                    col_num = box_to_examine % 3 * 3 + box_col_num
                    if utils.pointing_col_eliminate(box_to_examine, driver.get_pencil_data().get_col(col_num), digit):
                        return True
    return False

def multiple_lines(driver : BoardDriver):
    """Uses multiple lines technique to eliminate candidates"""
    return False
