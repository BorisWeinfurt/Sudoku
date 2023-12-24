"""Holds data and methods used to manipulate the board"""

class BoardDriver:
    """Holds data and methods used to manipulate the board"""
    def __init__(self, board):
        self.board = board
        count = 0
        for row in board:
            for element in row:
                if element != 0:
                    count += 1
        self.num_digits = count

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

    def get_row(self, row_index):
        """Get the current digits in the specified row"""
        return self.board[row_index]

    def get_col(self, col_index):
        """Get the current digits in the specified col"""
        col = []
        for row in self.board:
            col.append(row[col_index])
        return col

    def get_box(self, box):
        """Get the current digits in the specified box"""
        init_row = box // 3
        init_col = box % 3

        box_values = []
        for row in range(init_row * 3, init_row * 3 + 3):
            for col in range(init_col * 3, init_col * 3 + 3):
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
