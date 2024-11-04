from math import sqrt
def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    print(sqrt(sq))
    square_root = sqrt(sq)
    if square_root%1 != 0:
        return -1
    return ((sqrt(sq) + 1) ** 2)