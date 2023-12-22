"""Holds data and methods used to manipulate the board"""

class BoardDriver:
    """Holds data and methods used to manipulate the board"""
    def __init__(self):
        #temporary until custom puzzles are implemented
        sudoku_puzzle = [
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
        self.board = sudoku_puzzle
        self.num_digits = 30

    def add_digit(self, position, digit):
        """Add a digit to a specific position on the board"""
        if self.check_position_valid(position, digit):
            self.board[position.row][position.col] = digit
            self.num_digits += 1
            return True
        return False

    def check_position_valid(self, position, digit):
        """Check whether or not a digit can be placed at a certain position"""
        if self.board[position.row][position.col] != 0:
            return False
        row = self.get_row(position.row)
        col = self.get_col(position.col)
        box = self.get_box(position.row // 3 * 3 + position.col // 3)

        return digit not in row and digit not in col and digit not in box

    def get_row(self, rowIndex):
        """Get the current digits in the specified row"""
        return self.board[rowIndex]

    def get_col(self, colIndex):
        """Get the current digits in the specified col"""
        col = []
        for row in self.board:
            col.append(row[colIndex])
        return col

    def get_box(self, box):
        """Get the current digits in the specified box"""
        initRow = box // 3
        initCol = box % 3

        box_values = []
        for row in range(initRow * 3, initRow * 3 + 3):
            for col in range(initCol * 3, initCol * 3 + 3):
                box_values.append(self.board[row][col])
        return box_values

    def print_board(self):
        """Prints a terminal representation of the current board state"""
        for i, row in enumerate(self.board):
            if i % 3 == 0 and i != 0:
                print("-"*21)  # Add horizontal line every 3 rows
            print(" ".join(map(str, row[:3])) + " | " +
                " ".join(map(str, row[3:6])) + " | " +
                " ".join(map(str, row[6:])))

    def is_complete(self):
        """Checks whether or not the puzzle is complete based on the number or complete digits"""
        return self.num_digits == 81
