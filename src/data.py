"""
Module holds common data-structures used between files
"""

class Position:
    """Class holds the coordinate position of digits in the grid
    """
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def get_row(self):
        """Get the row"""
        return self.row

    def get_col(self):
        """Get the column"""
        return self.col

class PencilMarks:
    """Class holds the possible digits in a given square that doesnt yet have a digit
    """
    def __init__(self):
        # Initialize with all digits marked
        self.digits = list(range(1, 10))

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

sudoku_puzzle_test = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
