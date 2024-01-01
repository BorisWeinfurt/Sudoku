"""Contains the various techniques humans would use to solve a sudoku puzzle"""
from board_driver import BoardDriver
from data import Position
import utils
from pencil_marks import PencilMarks

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

def box_line_reduction(driver : BoardDriver):
    """Uses multiple lines technique to eliminate candidates"""
    for box in range(0,3):
        #rows
        row1 = driver.get_row(box * 3)
        row2 = driver.get_row(box * 3 + 1)
        row3 = driver.get_row(box * 3 + 2)
        
        for digit in range(1,10):
            #if the digit appears in one of the rows then there cannot be multiple lines
            if digit in row1 or digit in row2 or digit in row3:
                continue
            pencil_rows = [
                driver.get_pencil_data().get_row(box * 3),
                driver.get_pencil_data().get_row(box * 3 + 1),
                driver.get_pencil_data().get_row(box * 3 + 2)]
            
            for row_num, row in enumerate(pencil_rows):
                num_candidate_boxes = 0
                box_id = -1
                for pencil_row_sub_box in range(0, 3):
                    for pencil_mark in row[pencil_row_sub_box*3:pencil_row_sub_box*3+3]:
                        if pencil_mark is not None and digit in pencil_mark.get_pencil_marks():
                            num_candidate_boxes += 1
                            box_id = pencil_row_sub_box
                            break
                #If all possibilities for a row appear in one box then it cannot
                #Appear in the rest of the box
                if num_candidate_boxes == 1:
                    num_pencilmarks_eliminated = 0
                    for inner_row_num, row in enumerate(pencil_rows):
                        if inner_row_num != row_num:
                            for i in range(box_id * 3, box_id * 3 + 3):
                                if row[i] is not None and row[i].remove_digit(digit):
                                    num_pencilmarks_eliminated += 1
                                    
                    #If the technique resulted in eliminating pencilmarks return true
                    if num_pencilmarks_eliminated > 0:
                        return True
                    
        #columns
        col1 = driver.get_col(box * 3)
        col2 = driver.get_col(box * 3 + 1)
        col3 = driver.get_col(box * 3 + 2)
        for digit in range(1,10):
            #if the digit appears in one of the cols then there cannot be multiple lines
            if digit in col1 or digit in col2 or digit in col3:
                continue
            pencil_cols = [
                driver.get_pencil_data().get_col(box * 3),
                driver.get_pencil_data().get_col(box * 3 + 1),
                driver.get_pencil_data().get_col(box * 3 + 2)]
            for col_num, col in enumerate(pencil_cols):
                num_candidate_boxes = 0
                box_id = -1
                for pencil_col_sub_box in range(0, 3):
                    for pencil_mark in col[pencil_col_sub_box*3:pencil_col_sub_box*3+3]:
                        if pencil_mark is not None and digit in pencil_mark.get_pencil_marks():
                            num_candidate_boxes += 1
                            box_id = pencil_col_sub_box
                            break
                #If all possibilities for a col appear in one box then it cannot
                #Appear in the rest of the box
                if num_candidate_boxes == 1:
                    num_pencilmarks_eliminated = 0
                    for inner_col_num, col in enumerate(pencil_cols):
                        if inner_col_num != col_num:
                            for i in range(box_id * 3, box_id * 3 + 3):
                                if col[i] is not None and col[i].remove_digit(digit):
                                    num_pencilmarks_eliminated += 1
                    
                    #If the technique resulted in eliminating pencilmarks return true
                    if num_pencilmarks_eliminated > 0:
                        return True  
        
    return False

def naked_and_hidden_sets(driver: BoardDriver):
    pencil_data = driver.get_pencil_data()

    set_sizes = [2, 3]
    set_types = ["naked", "hidden"] # 0 is naked and 1 is hidden
    
    def process_sets(set_size, set_type, pencil_data : list[list[list[PencilMarks]]]):
        for i, data_type in enumerate(pencil_data):
            for j, list in enumerate(data_type):
                if getattr(utils, f"{set_type}_set")(set_size, list):
                    return True
                
        return False
    
    data : list[list[list[PencilMarks]]] = [[],[],[]]
    for i in range(9):
            data[0].append(pencil_data.get_row(i))
            data[1].append(pencil_data.get_col(i))
            data[2].append(pencil_data.get_box(i))
            
            
    for set_size in set_sizes:
        for set_type in set_types:
            if process_sets(set_size, set_type, data):
                return True

    return False
