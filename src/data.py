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

sudoku_puzzle_easy = [
    [0,0,6,0,0,0,5,0,8],
    [1,0,2,3,8,0,0,0,4],
    [0,0,0,2,0,0,1,9,0],
    [0,0,0,0,6,3,0,4,5],
    [0,6,3,4,0,5,8,7,0],
    [5,4,0,9,2,0,0,0,0],
    [0,8,7,0,0,4,0,0,0],
    [2,0,0,0,9,8,4,0,7],
    [4,0,9,0,0,0,3,0,0]
]

# [1, 2]
# [1, 2, 4]
# [4]
# [2]
# [2, 3]
# [3, 4]
# [2, 4, 8]
# [1, 2, 4, 7]
# [1, 2, 4, 7]
# [1, 2, 3, 4, 5]
# [1, 2, 9]
# [4, 5]
# [2, 4, 7]
# [2, 9]
# [5, 7, 9]
# [7]
# [2, 7]
# [1, 3, 9]
# [4, 5]
# [4, 8]
# [1, 4, 5, 7]
# [1, 3, 4]
# [1, 3, 4]
# [2, 3, 6, 7]
# [3]
# [2, 6, 7]
# []
# [3, 5]
# [1, 3, 4]
# [4]
# [4]
# [2, 7]
# [2, 3]
# [7, 9]
# [5]
# [5, 6, 7]
# [5, 7]
# [6]
# [5, 6, 7]
# [6, 7]
# [3, 6]
# [1, 7]
# [1, 7]
# [1, 2]
# [1, 2, 9]
# [1, 2, 9]
# [1]
# [1]
# [1]
# [2, 9]
# [1, 2]
# [7, 8]
# [1, 7]
# [1, 7, 8]
# [1, 7]
# [1, 3, 5]
# [1, 5]
# [1, 2, 6]
# [3, 6]
# [1, 3, 5]
# [1, 6]
# [6]
# [1, 6]
# [6]
# [1, 5]
# [2, 6]