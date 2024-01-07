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
solved_board1 = [
    [3,7,9,8,5,1,2,4,6],
    [6,8,5,2,3,4,9,1,7],
    [1,4,2,9,7,6,8,3,5],
    [9,1,6,5,2,8,3,7,4],
    [8,2,3,4,1,7,5,6,9],
    [7,5,4,6,9,3,1,8,2],
    [5,6,1,7,8,9,4,2,3],
    [2,3,7,1,4,5,6,9,8],
    [4,9,8,3,6,2,7,5,1],
]
sudoku_puzzle_test = [
[
    [0,0,6,0,0,0,5,0,8],
    [1,0,2,3,8,0,0,0,4],
    [0,0,0,2,0,0,1,9,0],
    [0,0,0,0,6,3,0,4,5],
    [0,6,3,4,0,5,8,7,0],
    [5,4,0,9,2,0,0,0,0],
    [0,8,7,0,0,4,0,0,0],
    [2,0,0,0,9,8,4,0,7],
    [4,0,9,0,0,0,3,0,0]
],
[
    [9,0,6,0,0,1,0,4,0],
    [7,0,1,2,9,0,0,6,0],
    [4,0,2,8,0,6,3,0,0],
    [0,0,0,0,2,0,9,8,0],
    [6,0,0,0,0,0,0,0,2],
    [0,9,4,0,8,0,0,0,0],
    [0,0,3,7,0,8,4,0,9],
    [0,4,0,0,1,3,7,0,6],
    [0,6,0,9,0,0,1,0,8]
],
[
    [0,0,0,0,3,0,8,7,1],
    [0,0,0,1,0,0,9,4,3],
    [0,0,0,4,0,0,0,0,2],
    [0,7,3,0,1,0,0,0,4],
    [6,0,5,0,0,0,7,0,8],
    [4,0,0,0,5,0,1,3,0],
    [1,0,0,0,0,7,0,0,0],
    [8,3,9,0,0,4,0,0,0],
    [7,5,4,0,2,0,0,0,0]
],
[
    [0,0,0,5,0,7,0,0,0],
    [0,4,0,2,6,3,0,0,0],
    [1,0,7,4,0,0,0,0,0],
    [3,6,0,0,0,0,0,4,5],
    [0,0,2,0,5,0,7,0,0],
    [7,9,0,0,0,0,0,6,2],
    [0,0,0,0,0,9,4,0,1],
    [0,0,0,1,3,4,0,9,0],
    [0,0,0,6,0,5,0,0,0]
],
[
    [0,1,0,4,0,0,2,0,0],
    [5,0,0,0,9,3,1,0,0],
    [0,0,0,0,0,0,0,5,6],
    [9,0,3,0,0,0,0,0,0],
    [0,0,0,6,8,9,0,0,0],
    [0,0,0,0,0,0,4,0,7],
    [7,5,0,0,0,0,0,0,0],
    [0,0,8,7,6,0,0,0,1],
    [0,0,9,0,0,1,0,4,0],
],
[#this is box line reduction 6
    [0,0,9,0,3,0,6,0,0],
    [0,3,6,0,1,4,0,8,9],
    [1,0,0,8,6,9,0,3,5],
    [0,9,0,0,0,0,8,0,0],
    [0,1,0,0,0,0,0,9,0],
    [0,6,8,0,9,0,1,7,0],
    [6,0,1,9,0,3,0,0,2],
    [9,7,2,6,4,0,3,0,0],
    [0,0,3,0,2,0,9,0,0],
],
[# this is very hard needs rectangles 6
    [4,0,0,2,7,0,6,0,0],
    [7,9,8,1,5,6,2,3,4],
    [0,2,0,8,4,0,0,0,7],
    [2,3,7,4,6,8,9,5,1],
    [8,4,9,5,3,1,7,2,6],
    [5,6,1,7,9,2,8,4,3],
    [0,8,2,0,1,5,4,7,9],
    [0,7,0,0,2,4,3,0,0],
    [0,0,4,0,8,7,0,0,2],
],
[#naked triple requiress swordfish 7
    [6,0,0,8,0,2,7,3,5],
    [7,0,2,3,5,6,9,4,0],
    [3,0,0,4,0,7,0,6,2],
    [1,0,0,9,7,5,0,2,4],
    [2,0,0,1,8,3,0,7,9],
    [0,7,9,6,2,4,0,0,3],
    [4,0,0,5,6,0,2,0,7],
    [0,6,7,2,4,0,3,0,0],
    [9,2,0,7,3,8,4,0,6],
],
[#hidden triple requiress
    [0,0,0,0,0,1,0,3,0],
    [2,3,1,0,9,0,0,0,0],
    [0,6,5,0,0,3,1,0,0],
    [6,7,8,9,2,4,3,0,0],
    [1,0,3,0,5,0,0,0,6],
    [0,0,0,1,3,6,7,0,0],
    [0,0,9,3,6,0,5,7,0],
    [0,0,6,0,1,9,8,4,3],
    [3,0,0,0,0,0,0,0,0],
],
[# trivial with an xwing
    [0,0,5,0,0,0,4,0,0],
    [0,2,0,9,4,0,0,0,0],
    [9,0,0,7,0,0,0,0,8],
    [0,0,3,0,0,0,2,9,0],
    [1,0,0,2,0,3,0,0,7],
    [0,7,9,0,0,0,3,0,0],
    [4,0,0,0,0,8,0,0,1],
    [0,0,0,0,1,4,0,6,0],
    [0,0,6,0,0,0,7,0,0],
],
[#trivial with double xwing
    [0,1,0,0,3,7,0,0,0],
    [0,0,0,0,0,0,0,1,0],
    [6,0,0,0,0,8,0,2,9],
    [0,7,0,0,4,9,6,0,0],
    [1,0,0,0,0,0,0,0,3],
    [0,0,9,3,5,0,0,7,0],
    [3,9,0,2,0,0,0,0,8],
    [0,4,0,0,0,0,0,0,0],
    [0,0,0,7,9,0,0,6,0],
],
[#trivial with a swordfish 11
    [0,3,0,2,0,0,9,7,0],
    [0,0,0,3,0,6,0,0,0],
    [8,0,0,0,5,0,0,0,0],
    [0,0,1,0,4,0,0,8,7],
    [0,5,0,0,0,0,0,4,0],
    [9,7,0,0,6,0,3,0,0],
    [0,0,0,0,1,0,0,0,6],
    [0,0,0,7,0,3,0,0,0],
    [0,1,9,0,0,8,0,3,0],
],
[# rectangle elimintation practice 12
    [7,0,0,1,0,2,0,0,3],
    [0,2,0,0,0,0,0,7,0],
    [3,0,6,0,0,0,1,0,2],
    [0,0,0,3,0,8,0,0,6],
    [0,5,0,0,0,0,0,9,0],
    [8,0,0,2,0,9,0,0,0],
    [6,0,8,0,0,0,5,0,1],
    [0,3,0,0,0,0,0,8,0],
    [1,0,0,6,0,5,0,0,4],
]
]
