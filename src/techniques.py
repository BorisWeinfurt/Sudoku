"""Contains the various techniques humans would use to solve a sudoku puzzle"""
from board_driver import BoardDriver
import utils
from data import Position
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
    "Finds the naked and hidden sets of size 2 and 3 in a given puzzle and eliminates relevant pencilmarks"
    pencil_data = driver.get_pencil_data()

    set_sizes = [2, 3]
    set_types = ["naked", "hidden"] # 0 is naked and 1 is hidden
    
    def process_sets(set_size, set_type, pencil_data : "list[list[list[PencilMarks]]]"):
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

def xwing(driver : BoardDriver):
    "Attempts to use xwing to eliminate some pencilmarks"
    
    for digit in range(1,10):
        
        for row in range(0,8): #skip last row
            if digit in driver.get_row(row):
                continue
            pencil_row = driver.get_pencil_data().get_row(row)
            res = utils.list_has_set(pencil_row, digit, [2])
            if res is not None:
                for x_row in range(row+1, 9):
                    if digit in driver.get_row(x_row):
                        continue
                    pencil_x_row = driver.get_pencil_data().get_row(x_row)
                    x_res = utils.list_has_set(pencil_x_row, digit, [2])
                    
                    # check if the pairs are in the same rows to form an xwing
                    if res is not None and res == x_res:
                        eliminated = False
                        for loop_row in range(0,9):
                            
                            if loop_row != row and loop_row != x_row:
                                #get pencil_mark to try to remove
                                mark = driver.get_pencil_data().get_row(loop_row)[res[0]]
                                xmark = driver.get_pencil_data().get_row(loop_row)[res[1]]
                                # attempt to remove pencilmarks
                                row_eliminated = mark is not None and mark.remove_digit(digit)
                                x_row_eliminated = xmark is not None and xmark.remove_digit(digit)
                                eliminated = eliminated or row_eliminated or x_row_eliminated
                        if eliminated:
                            return True
        
        for col in range(0,8): #skip last col
            if digit in driver.get_col(col):
                continue
            pencil_col = driver.get_pencil_data().get_col(col)
            res = utils.list_has_set(pencil_col, digit, [2])
            if res is not None:
                for x_col in range(col+1, 9):
                    if digit in driver.get_col(x_col):
                        continue
                    pencil_x_col = driver.get_pencil_data().get_col(x_col)
                    x_res = utils.list_has_set(pencil_x_col, digit, [2])
                    
                    # check if the pairs are in the same rows to form an xwing
                    if res is not None and res == x_res:
                        eliminated = False
                        for loop_col in range(0,9):
                            if loop_col != col and loop_col != x_col:
                                # get pencil_mark to try and remove the digit
                                mark = driver.get_pencil_data().get_col(loop_col)[res[0]]
                                xmark = driver.get_pencil_data().get_col(loop_col)[res[1]]
                                # try to remove the digit from the pencilmark
                                col_eliminated = mark is not None and mark.remove_digit(digit)
                                x_col_eliminated = xmark is not None and xmark.remove_digit(digit)
                                eliminated = eliminated or col_eliminated or x_col_eliminated
                        if eliminated:
                            return True
                        
def swordfish(driver : BoardDriver):
    """Utilizes the swordfish technique to elimintate candidates"""
    
    def directional_swordfish(dig_list : "list[list[int]]", pencil_list : "list[list[PencilMarks]]"):
        """Given a 2d array of digits representing a sudoku (either rows or columns)"""
        """Uses swordfish to try and delete pencilmarks returns true if there are succsesful deletions"""
        for digit in range(1,10):
            
            for parent_row_num in range(0,7): #skip last two rows
                if digit in dig_list[parent_row_num]:
                    continue
                
                pencil_row = pencil_list[parent_row_num]
                parent_row = utils.list_has_set(pencil_row, digit, [2,3])
                
                if parent_row is not None:
                    for first_child_row_num in range(parent_row_num+1, 8):
                        if parent_row_num == first_child_row_num or digit in dig_list[first_child_row_num]:
                            continue
                        pencil_child1_row = pencil_list[first_child_row_num]
                        first_child_row = utils.list_has_set(pencil_child1_row, digit, [2,3])
                        
                        if first_child_row is not None and len(set(first_child_row).union(set(parent_row))) <= 3:
                            
                            for second_child_row_num in range(first_child_row_num+1, 8):
                                conditions = [
                                    parent_row_num == first_child_row_num,
                                    first_child_row_num == second_child_row_num,
                                    digit in dig_list[second_child_row_num]
                                ]
                                if any(conditions):
                                    continue
                                
                                pencil_child2_row = pencil_list[second_child_row_num]
                                second_child_row = utils.list_has_set(pencil_child2_row, digit, [2,3])
                                
                                if second_child_row is None:
                                    break
                                
                                swordfish_cols = set(second_child_row).union(set(first_child_row).union(set(parent_row)))
                                if len(swordfish_cols) <= 3:
                                    swordfish_rows = [parent_row_num, first_child_row_num, second_child_row_num]
                                    elimination = False
                                    for elimination_row in range(0,9):
                                        if elimination_row in swordfish_rows:
                                            continue
                                        
                                        for elimination_col in swordfish_cols:
                                            mark : PencilMarks= pencil_list[elimination_row][elimination_col]
                                            if mark is not None and mark.remove_digit(digit):
                                                elimination = True
                                    if elimination:
                                        return True
        return False
    
    row_dig = []
    col_dig = []
    row_pencil = []
    col_pencil = []
    for i in range(0,9):
        row_dig.append(driver.get_row(i))
        col_dig.append(driver.get_col(i))
        row_pencil.append(driver.get_pencil_data().get_row(i))
        col_pencil.append(driver.get_pencil_data().get_col(i))
        
    return directional_swordfish(row_dig, row_pencil) or directional_swordfish(col_dig, col_pencil)

def rectange_elimination(driver : BoardDriver):
    """Uses empty rectanges to try and eliminate pencil marks"""

    def directional_rectangle_eliminate(digit_list : "list[list[int]]", pencil_list : "list[list[PencilMarks]]"):
        for digit in range(1,10):
            for row_num in range(0,9):
                if digit in digit_list[row_num]:
                    continue
                
                # find if there is a hinge cell candidate
                for col_num, row_mark in enumerate(pencil_list[row_num]):
                    if row_mark is None or digit not in row_mark.get_pencil_marks():
                        continue
                    
                    # if one is found, check if it would anything from its column that isnt in the same box
                    column = [x[col_num] for x in pencil_list]
                    for forcing_row_num, col_mark in enumerate(column):
                        vertical_box = row_num // 3 * 3
                        if (col_mark is None or digit not in col_mark.get_pencil_marks()) or forcing_row_num in range(vertical_box, vertical_box+3):
                            continue
                        # if something is eliminated see if its forced somewhere else in its row that isnt in the same box
                        row_candidates = utils.list_has_set(pencil_list[forcing_row_num], digit, [2])
                        if row_candidates is None or col_num not in row_candidates:
                            continue
                        
                        
                        row_candidates.remove(col_num)
                        forcing_col = row_candidates[0]
                        # check that its not in the same box
                        horizontal_box = col_num // 3 * 3
                        if forcing_col in range(horizontal_box, horizontal_box+3):
                            continue
                        # now check whether the newly forced digit creates an impossible box
                        box_num = (row_num // 3) * 3 + forcing_col // 3
                        start_row = (box_num // 3) * 3
                        start_col = (box_num % 3) * 3

                        box_values = []
                        for row in range(start_row, start_row  + 3):
                            for col in range(start_col, start_col + 3):
                                box_values.append(digit_list[row][col])
                                
                        if digit in box_values:
                            continue
                        num_candidates = 0
                        for box_row_num in range(start_row, start_row+3):
                            if box_row_num == row_num:
                                continue
                            box_row = pencil_list[box_row_num]
                            for box_col_num in range(start_col, start_col+3):
                                if box_col_num == forcing_col:
                                    continue
                                
                                if box_row[box_col_num] is not None and digit in box_row[box_col_num].get_pencil_marks():
                                    num_candidates += 1
                        # we have created an impossible box therfore the original mark was wrong
                        if num_candidates == 0:
                            row_mark.remove_digit(digit)
                            return True
                        
    row_dig = []
    col_dig = []
    row_pencil = []
    col_pencil = []
    for i in range(0,9):
        row_dig.append(driver.get_row(i))
        col_dig.append(driver.get_col(i))
        row_pencil.append(driver.get_pencil_data().get_row(i))
        col_pencil.append(driver.get_pencil_data().get_col(i))

    return directional_rectangle_eliminate(row_dig, row_pencil) or directional_rectangle_eliminate(col_dig, col_pencil)