from typing import List, Tuple
import random

Matrix = List[List[int]]

# indexes for 3x3 flat matrix
row_idx = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
col_idx = [tuple(j) for j in zip(*row_idx)]
diags = [(0, 4, 8), (2, 4, 6)]
indexes = (row_idx, col_idx, diags)


def flatten(l: Matrix) -> List[int]:
    """ Flattens list of list"""
    return [i for ls in l for i in ls]


def is_magic(square: List[int]) ->bool:
    if len(set(square)) != len(square):
        return False
    else:
        flat_idx = [idt for l in indexes for idt in l]
        for idx in flat_idx:
            if sum(square[i] for i in idx) != 15:
                return False
        else:
            return True


def get_all_magics() -> Matrix:
    """returns all possible 3x3 magic squares
    with unique elements in range [1, 9]
    """
    corner_i = (0, 2, 6, 8)  # place evens here
    edge_i = (1, 3, 5, 7)  # place odds here
    all_squares = []

    while True:
        if len(all_squares) == 8:
            break

        odds = [1, 3, 7, 9]
        evens = [2, 4, 6, 8]

        square = [0] * 9
        square[4] = 5  # center is always 5

        for i, e in enumerate(square):
            if i == 4:  # don't touch the center
                continue

            elif i in corner_i:  # even
                n = random.choice(evens)
                evens.remove(n)
                square[i] = n

            elif i in edge_i:  # odds
                n = random.choice(odds)
                odds.remove(n)
                square[i] = n

        if is_magic(square) and square not in all_squares:
            all_squares.append(square)

    return all_squares


def calc_score(oldval: int, newval: int) -> int:
    return abs(oldval - newval)


def formingMagicSquare(s: Matrix) -> int:
    """Given a square, returns the minimum number of changes
    ti transform the square into a magic square
    """
    square = flatten(s)
    all_magics = get_all_magics()
    scores = []
    for magic_sq in all_magics:
        score = sum([calc_score(old, new)
                     for old, new in zip(magic_sq, square)])
        scores.append(score)

    return(min(scores))
