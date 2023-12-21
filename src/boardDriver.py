class BoardDriver:

    def __init__():
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

    def add_digit(Position, digit):
        if checkPositionValid(Position):
            board[Position.row][Position.col] = digit
            return True
        return False

    def checkPositionValid(Position, digit):
        row = getRow(Position.row)
        col = getCol(Position.col)
        box = getBox(Position.row // 3 * 3 + Position.col // 2)

        return digit not in row and digit not in col and digit not in box

    def getRow(rowIndex):
        return board[rowIndex]
    
    def getCol(colIndex):
        col = []
        for row in board:
            col.append(row[colIndex])
    
    def getBox(box):


    def printBoard(board):
        for i, row in enumerate(board):
            if i % 3 == 0 and i != 0:
                print("-"*21)  # Add horizontal line every 3 rows
            print(" ".join(map(str, row[:3])) + " | " +
                " ".join(map(str, row[3:6])) + " | " +
                " ".join(map(str, row[6:])))

    def isComplete():
        