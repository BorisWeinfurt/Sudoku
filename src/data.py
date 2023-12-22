

class Position:
    def __init__(self, row, col):
        self.row = row
        self.col = col

class PencilMarks:
    def __init__(self):
        # Initialize with all digits marked
        self.digits = list(range(1, 10))

    def addDigit(self, digit):
        # Add a digit to the pencil marks if it's not already present
        if 1 <= digit <= 9 and digit not in self.digits:
            self.digits.append(digit)

    def removeDigit(self, digit):
        # Remove a digit from the pencil marks if it's present
        if 1 <= digit <= 9 and digit in self.digits:
            self.digits.remove(digit)

    def getPencilMarks(self):
        # Return the list of remaining pencil marks
        return self.digits