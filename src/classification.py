"""Utilize human solving techniques to give useful information
about sudoku boards
"""
import board_driver
import techniques
import utils
import copy
import random
from boards import solved_boards
from pprint import pprint



def generate_difficulty(difficulty):
    difficulties = {
        0: (3000, 4500),  # easy
        1: (4300, 6000),  # medium
        2: (5700, 9000),  # hard
        3: (8500, 15000),  # tricky
        4: (14000, 30000),  # fiendish
    }
    solved_board = random_element = random.choice(solved_boards)
    
    max_attempts_per_level = 5
    puzzle = []
    
    def recursive_generator(board, max_attempts):
        nonlocal puzzle
        attempts = 0
        
        while attempts < max_attempts:
            board_copy = copy.deepcopy(board)
            utils.remove_digit_from_board(board_copy)
            new_difficulty = classify_difficulty(copy.deepcopy(board_copy))
            if new_difficulty == -1:
                return False
            
            if difficulties[difficulty][0] <= new_difficulty <= difficulties[difficulty][1]:
                # Successful: Created a good board within the desired difficulty range
                puzzle = board_copy
                return True

            elif new_difficulty > difficulties[difficulty][1]:
                # New board is too hard, try again
                attempts += 1
                
            else:
                # good selection needs more removal
                if (recursive_generator(board_copy, max_attempts)):
                    return True
        
        return False
    
    # Loop until succsessful puzzle
    while True:
        if recursive_generator(solved_board, max_attempts_per_level):
            return puzzle

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
        
        return -1
    
    return difficulty 
