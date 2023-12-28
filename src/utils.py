"""Helper functions"""
from pencil_marks import PencilMarks
def missing_digits(cur_digits):
    """Find the missing digits from the range 1-9 in from any list"""
    required_digits = [1,2,3,4,5,6,7,8,9]
    found_missing_digits = []
    for digit in required_digits:
        if digit not in cur_digits:
            found_missing_digits.append(digit)
    return found_missing_digits


def get_row(box, row_num):
    """Given a 1d representation of a sudoku box return a given row"""
    row_start = row_num * 3
    row_end = row_start + 3
    return box[row_start:row_end]

def get_col(box, col_num):
    """Given a 1d representation of a sudoku box return a given column"""
    col_indices = [col_num, col_num + 3, col_num + 6]
    return [box[i] for i in col_indices]

def count_in_pencilmarks(lst : list[PencilMarks], digit):
    """Checks how times the list of pencil_marks contains the given digit."""
    count = 0
    for marks in lst:
        if marks is not None and digit in marks.get_pencil_marks():
            count+=1
    return count

def pointing_row_eliminate(box_to_ignore : int, pencil_row : list[PencilMarks], digit_to_elim):
    """eliminate all pencil marks of a digit in a row excluding a specific box
    returns true if some digit was eliminated"""
    num_elim = 0
    box_indices = [i for i in range(box_to_ignore % 3 * 3, box_to_ignore % 3 * 3 + 3)]
    for i, pencil_mark in enumerate(pencil_row):
        # Check if the cell is in the specified box to ignore
        if i not in box_indices and pencil_mark is not None and digit_to_elim in pencil_mark.get_pencil_marks():
            pencil_mark.remove_digit(digit_to_elim)
            num_elim += 1
            # print("Exlude: ", box_indices)
            # print("removing column ", i)
            # print(pencil_mark.get_pencil_marks())
    # print("num elim", num_elim)
    return num_elim > 0
 
def pointing_col_eliminate(box_to_ignore : int, pencil_col : list[PencilMarks], digit_to_elim):
    """eliminate all pencil marks of a digit in a column excluding a specific box
    returns true if some digit was eliminated"""
    num_elim = 0
    box_indices = [i for i in range(box_to_ignore // 3 * 3, box_to_ignore // 3 * 3 + 3)]

    for i, pencil_mark in enumerate(pencil_col):
        # Check if the cell is in the specified box to ignore
        if i not in box_indices and pencil_mark is not None and digit_to_elim in pencil_mark.get_pencil_marks():
            pencil_mark.remove_digit(digit_to_elim)
            num_elim += 1
    return num_elim > 0
