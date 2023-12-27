
def missing_digits(cur_digits):
    """Find the missing digits from the range 1-9 in from any list"""
    required_digits = [1,2,3,4,5,6,7,8,9]
    found_missing_digits = []
    for digit in required_digits:
        if digit not in cur_digits:
            found_missing_digits.append(digit)
    return found_missing_digits
