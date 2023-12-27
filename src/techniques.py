"""Contains the various techniques humans would use to solve a sudoku puzzle"""
from board_driver import BoardDriver
from data import Position
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
    for i in range(0,9):
        box_digits = driver.get_board_data(i)
        pencil_digits = driver.get_pencil_data().get_box(i)
        for digit in range(1,10):
            if digit in box_digits:
                continue
            failure_flag = False
            # rows
            for row_num in range(0,3):
                digit_count = 0
                for col_num in range(0,3):#check for pairs or triples in a row
                    if digit in pencil_digits[row_num*3+col_num].get_pencil_marks():
                        digit_count+=1
                if digit == 1:
                    # if there is a single pencil mark and its not a single position then it cant be a pointing row
                    break
                if digit >= 2:
                    # if there is a pointing row check that there are no other entries in the box
                    for index in range((row_num + 1) * 3, 9):
                        if digit in pencil_digits[index].get_pencil_marks():
                            # duplicate has been found there can no longer be a pointing row or col for this digit
                            failure_flag = True
                            break
                    if failure_flag:
                        break
                    else:
                        # attempt to eliminate candidates using this pair
                        # if some were eliminated technique is a success
                        return True

            if failure_flag: # if failure flag this box cannot have a pointing column
                continue
            # columns
            for col_num in range(0,3):
                digit_count = 0
                for row_num in range(0,3):#check for pairs or triples in a column
                    if digit in pencil_digits[row_num*3+col_num].get_pencil_marks():
                        digit_count+=1
                if digit == 1:
                    # if there is a single pencil mark and its not a single position then there cant be a pointing column
                    break
                if digit >= 2:
                    # if there is a pointing column check that there are no other entries in the box
                    for index in range((row_num + 1) * 3, 9):
                        if digit in pencil_digits[index].get_pencil_marks():
                            # duplicate has been found there can no longer be a pointing row or col for this digit
                            failure_flag = True
                            break
                    if failure_flag:
                        break
                    else:
                        # attempt to eliminate candidates using this pair
                        # if some were eliminated technique is a success
                        return True
                    
    return False

def multiple_lines(driver : BoardDriver):
    """Uses multiple lines technique to eliminate candidates"""
    return False
