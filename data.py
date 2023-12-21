class Board:

    def __init__(digits):

    
    def addDigit(Position, digit):

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class PencilMarks:
    def __init__(self):
        # Initialize with all digits marked
        self.digits = list(range(1, 10))

    def add_digit(self, digit):
        # Add a digit to the pencil marks if it's not already present
        if 1 <= digit <= 9 and digit not in self.digits:
            self.digits.append(digit)

    def remove_digit(self, digit):
        # Remove a digit from the pencil marks if it's present
        if 1 <= digit <= 9 and digit in self.digits:
            self.digits.remove(digit)

    def get_pencil_marks(self):
        # Return the list of remaining pencil marks
        return self.digits