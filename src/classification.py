"""Utilize human solving techniques to give useful information
about sudoku boards
"""
import board_driver
import techniques

def generate_difficulty(difficulty):
    """"Generates a puzzle of the given difficulty and returns it"""
    board = difficulty
    return board


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
