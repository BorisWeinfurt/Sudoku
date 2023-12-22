import data

class BoardDriver:

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

    def add_digit(self, Position, digit):
        if self.checkPositionValid(Position, digit):
            self.board[Position.row][Position.col] = digit
            self.num_digits += 1
            return True
        return False

    def checkPositionValid(self, Position, digit):
        if self.board[Position.row][Position.col] != 0:
            return False
        row = self.getRow(Position.row)
        col = self.getCol(Position.col)
        box = self.getBox(Position.row // 3 * 3 + Position.col // 3)

        return digit not in row and digit not in col and digit not in box

    def getRow(self, rowIndex):
        return self.board[rowIndex]
    
    def getCol(self, colIndex):
        col = []
        for row in self.board:
            col.append(row[colIndex])
        return col
    
    def getBox(self, box):
        initRow = box // 3
        initCol = box % 3

        box_values = []
        for row in range(initRow * 3, initRow * 3 + 3):
            for col in range(initCol * 3, initCol * 3 + 3):
                box_values.append(self.board[row][col])
        return box_values

    def printBoard(self):
        for i, row in enumerate(self.board):
            if i % 3 == 0 and i != 0:
                print("-"*21)  # Add horizontal line every 3 rows
            print(" ".join(map(str, row[:3])) + " | " +
                " ".join(map(str, row[3:6])) + " | " +
                " ".join(map(str, row[6:])))

    def isComplete(self):
        return self.num_digits == 81