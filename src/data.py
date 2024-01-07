"""File to hold datastructures used in the program"""

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

