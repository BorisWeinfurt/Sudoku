"""Data for maintaining pencil marks accross tiles and/or board"""

from typing import List
from data import Position
class PencilMarkBoard:
    """Maintains a 2d array of pencilmarks to represent the whole board"""
    def __init__(self, driver):
        self.pencil_data = self.fill_pencil_marks(driver)

    def fill_pencil_marks(self, board_driver):
        """Create pencilmarks for all missing digits in the puzzle"""
        size = 10  # Constant for the size of the puzzle
        columns = [board_driver.get_col(i) for i in range(0, size-1)]
        boxes = [board_driver.get_box(i) for i in range(0, size-1)]

        pencil_data : List[List[PencilMarks]] = []
        for row_id, row in enumerate(board_driver.get_board_data()):
            row_of_pencil_marks = []
            for col_id, digit in enumerate(row):
                if digit != 0:
                    row_of_pencil_marks.append(None)
                    continue
                box_id = (row_id // 3) * 3 + (col_id // 3)

                pencil_mark = PencilMarks()
                for possible_digit in range(1, size):
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

    def update_pencil_data(self, position: Position, digit: int):
        """Update pencil marks for the whole board when a digit is added"""
        row_num = position.get_row()
        col_num = position.get_col()
        box_num = (row_num // 3) * 3 + (col_num // 3)
        self.pencil_data[row_num][col_num] = None
        # Remove digit from pencil marks in the same row
        for pencil_marks in self.pencil_data[row_num]:
            if pencil_marks is not None:
                pencil_marks.remove_digit(digit)

        # Remove digit from pencil marks in the same column
        for row in self.pencil_data:
            if row[col_num] is not None:
                row[col_num].remove_digit(digit)

        # Remove digit from pencil marks in the same 3x3 box
        box_start_row = (box_num // 3) * 3
        box_start_col = (box_num % 3) * 3

        for box_row in range(box_start_row, box_start_row + 3):
            for box_col in range(box_start_col, box_start_col + 3):
                if self.pencil_data[box_row][box_col] is not None:
                    self.pencil_data[box_row][box_col].remove_digit(digit)

    def dump_pencil_data(self):
        """Return all the pencil marks in array form for data manipulation"""
        return self.pencil_data

    def get_row(self, row_index):
        """Get the current digits in the specified row"""
        return self.pencil_data[row_index]

    def get_col(self, col_index):
        """Get the current digits in the specified col"""
        col = []
        for row in self.pencil_data:
            col.append(row[col_index])
        return col

    def get_box(self, box):
        """Get the current digits in the specified box"""
        init_row = box // 3
        init_col = box % 3

        box_values : List[PencilMarks] = []
        for row in range(init_row * 3, init_row * 3 + 3):
            for col in range(init_col * 3, init_col * 3 + 3):
                box_values.append(self.pencil_data[row][col])
        return box_values


class PencilMarks:
    """Class holds the possible digits in a given square that doesnt yet have a digit
    """
    def __init__(self):
        # Initialize with all digits marked
        self.digits = []

    def add_digit(self, digit):
        """
        Add a new digit to the pencilmark
        """
        # Add a digit to the pencil marks if it's not already present
        if 1 <= digit <= 9 and digit not in self.digits:
            self.digits.append(digit)

    def remove_digit(self, digit):
        """Remove a digit from the pencilmark"""
        # Remove a digit from the pencil marks if it's present
        if 1 <= digit <= 9 and digit in self.digits:
            self.digits.remove(digit)

    def get_pencil_marks(self):
        """Get the current pencilmarks"""
        # Return the list of remaining pencil marks
        return self.digits
    