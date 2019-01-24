from typing import List, Tuple


def sum_ax(l: List[List[int]], axis: int) -> List[int]:
    """ sum lists of lists numpy like
    """
    if axis == 1:
        return [sum(i) for i in zip(*l)]
    if axis == 0:  # sum transposed form (suicide for big matrix)
        return [sum(i) for i in zip(*[list(j) for j in zip(*l)])]


def magic_constant(n: int) -> int:
    return n*((n**2 + 1) / 2)


def all_equal(l: List[int]) -> Tuple[bool, int]:
    """returns if all elements are equal and if not, 
    the index of the different elements
    """
    equality = True if len(set(l)) == 1 else False

    if equality:
        return (True, None)

    else:
        raise NotImplementedError
        return (False)


# --------------------
#  The func to submit
# --------------------


def formingMagicSquare(s: List[List[int]]) -> int:
    """Given a square, returns the minimum number of changes
    ti transform the square into a magic square
    """

    assert isinstance(s, list)
