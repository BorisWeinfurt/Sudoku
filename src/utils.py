"""Helper functions"""
from itertools import combinations
from functools import reduce
import itertools
from pencil_marks import PencilMarks
from typing import Dict, List
from pprint import pprint

def missing_digits(cur_digits):
    """Find the missing digits from the range 1-9 in from any list"""
    required_digits = [1,2,3,4,5,6,7,8,9]
    found_missing_digits = []
    for digit in required_digits:
        if digit not in cur_digits:
            found_missing_digits.append(digit)
    return found_missing_digits

def get_box(list, box_num):
    """Given a list of nine numbers (row or col) there will be 3 boxes along that column,
       returns the three digits in the specified box (0,1,2)"""
    row_start = box_num * 3
    row_end = row_start + 3
    return list[row_start:row_end]
       
def get_row(box, row_num):
    """Given a 1d representation of a sudoku box return a given row (0,1,2)"""
    row_start = row_num * 3
    row_end = row_start + 3
    return box[row_start:row_end]

def get_col(box, col_num):
    """Given a 1d representation of a sudoku box return a given column (0,1,2)"""
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
    box_indices = list(range(box_to_ignore % 3 * 3, box_to_ignore % 3 * 3 + 3))
    for i, pencil_mark in enumerate(pencil_row):
        # Check if the cell is in the specified box to ignore
        if i not in box_indices and pencil_mark is not None and pencil_mark.remove_digit(digit_to_elim):
            num_elim += 1
    return num_elim > 0
 
def pointing_col_eliminate(box_to_ignore : int, pencil_col : list[PencilMarks], digit_to_elim):
    """eliminate all pencil marks of a digit in a column excluding a specific box
    returns true if some digit was eliminated"""
    num_elim = 0
    box_indices = list(range(box_to_ignore // 3 * 3, box_to_ignore // 3 * 3 + 3))

    for i, pencil_mark in enumerate(pencil_col):
        # Check if the cell is in the specified box to ignore
        if i not in box_indices and pencil_mark is not None and pencil_mark.remove_digit(digit_to_elim):
            num_elim += 1
    return num_elim > 0

def naked_set(size : int, pencil_marks : list[PencilMarks]):
    """Checks if there is a naked set that is size large and removes those pencil marks from the rest of the row"""
    """If some pencilmarks were removed then return true"""
    
    raw_marks : list[list[int]] = []
    for mark in pencil_marks:
        if mark is None:
            raw_marks.append(mark)
        else:
            raw_marks.append(mark.get_pencil_marks())

    for set_num, parent_set in enumerate(raw_marks):
        
        indexes = []
        if parent_set is not None and len(parent_set) <= size:
            indexes.append(set_num)
            
            #determine whether other pencil marks make a set with the original
            for subset_num, subset in enumerate(raw_marks):
                if subset is not None and subset_num != set_num and set(subset).issubset(set(parent_set)):
                    indexes.append(subset_num)

                    # if a naked set is found try to eliminate digits from other pencil marks
                    if len(indexes) == size:
                        num_eliminated = 0
                        for mark_num, mark in enumerate(pencil_marks):
                            if mark is not None and mark_num not in indexes:
                                for num_to_elim in parent_set:
                                    if mark.remove_digit(num_to_elim):
                                        num_eliminated += 1
                        #if digits have been eliminated then exit
                        if num_eliminated > 0:
                            return True
                        
def hidden_set(size : int, pencil_marks : list[PencilMarks]):
    """Checks if there is a hidden set that is size large and removes excess pencil marks from the set"""
    pruned_pencil_marks : list[PencilMarks] = [x for x in pencil_marks if x != None]
   
    graph : list[List[int]] = [ [] for _ in range(9) ]
    # create a graph of where each digit can be placed
    for digit in range(1,10):
        for mark_num, mark in enumerate(pruned_pencil_marks):
            if digit in mark.get_pencil_marks():
                graph[digit-1].append(mark_num)
                
    possible_digits = reduce(lambda x, y: x | set(y.get_pencil_marks()), pruned_pencil_marks, set())
    # loop through combinations in the graph to check if they are hidden sets
    for digit_combination in itertools.combinations(possible_digits, size):
        index_possible_squares = []
        for digit in digit_combination:

            for destination in graph[digit-1]:
                if destination not in index_possible_squares:
                    index_possible_squares.append(destination)
                    
        # hidden set is found, try to eliminate pencilamarks
        if len(index_possible_squares) == size:
            num_eliminated = 0
            digits_to_remove = [x for x in range(1,10) if x not in digit_combination]
            for digit_to_remove in digits_to_remove:
                for pencil_mark_index in index_possible_squares:
                    if pruned_pencil_marks[pencil_mark_index].remove_digit(digit_to_remove):
                        num_eliminated += 1
            if num_eliminated > 0:
                return True

def list_has_pair(list : list[PencilMarks], digit):
    """Checks if the given list has a pair, if yes return indexes of the pair otherwise return none"""
    indexes = []
    for index, mark in enumerate(list):
        if mark is not None and digit in mark.get_pencil_marks():
            indexes.append(index)
    
    if len(indexes) != 2:
        return None
    return indexes