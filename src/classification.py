"""Utilize human solving techniques to give useful information
about sudoku boards
"""
import board_driver
import techniques
import utils
import copy
from pprint import pprint



def generate_difficulty(solved_board, difficulty):
    difficulties = {
        0: (3000, 4500),  # easy
        1: (4300, 6000),  # medium
        2: (5700, 9000),  # hard
        3: (8500, 15000),  # tricky
    }

    max_attempts = 1000
    attempts = 0
    
    while attempts < max_attempts:
        board_copy = copy.deepcopy(solved_board)
        utils.remove_digit_from_board(board_copy)
        pprint(board_copy)
        new_difficulty = classify_difficulty(board_copy)

        if difficulties[difficulty][0] <= new_difficulty <= difficulties[difficulty][1]:
            # Successful: Created a good board within the desired difficulty range
            pprint(board_copy)
            return board_copy

        elif new_difficulty > difficulties[difficulty][1]:
            # New board is too hard, try again
            print("Too hard")
            attempts += 1
            continue

        else:
            # Good step, needs more removal
            for i in range(len(solved_board)):
                solved_board[i] = board_copy[i][:]
            attempts += 1

    print("Unable to create a board within the desired difficulty range")
    return None

def classify_difficulty(board):
    """Determines the difficulty of the provided puzzle"""
    driver = board_driver.BoardDriver(board)

    difficulty = 0
    while not driver.is_complete():
        
        if techniques.single_candidate(driver):
            # print("single candidate success")
            difficulty += 70
            continue
        if techniques.single_position(driver):
            # print("single position success")
            difficulty += 100
            continue
        if techniques.pointing_pairs_and_triples(driver):
            # print("pointing candidates success")
            difficulty += 350
            continue
        if techniques.box_line_reduction(driver):
            # print("box_line reduction success")
            difficulty += 700
            continue
        if techniques.naked_and_hidden_sets(driver):
            # print("Naked hidden sets succes")
            difficulty += 900
            continue
        if techniques.xwing(driver):
            # print("succsesful xwing")
            difficulty += 2800
            continue
        if techniques.rectange_elimination(driver):
            # print("rectangle success")
            difficulty += 5000
            continue
        if techniques.swordfish(driver):
            # print("succsesful xwing")
            difficulty += 7000
            continue
        
        print("Puzzle cannot be solved")
        driver.print_board()
        return -1
    
    # driver.print_board()
    print("Difficulty: ", difficulty)
    return difficulty 
