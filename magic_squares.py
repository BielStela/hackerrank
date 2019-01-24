from typing import List, Tuple

Matrix = List[List[int]]

RAW = """5 3 4
1 5 8
6 4 2
"""

matrix = []


for s in RAW.rstrip().split('\n'):
    matrix.append([int(i) for i in s.split()])


def sum_ax(l: Matrix, axis: int) -> List[int]:
    """ sum lists of lists numpy like
    """
    if axis == 1:
        return [sum(i) for i in zip(*l)]
    if axis == 0:  # sum transposed form (suicide for big matrix)
        return [sum(i) for i in zip(*[list(j) for j in zip(*l)])]


def sum_diagonal(l: Matrix, d: int) -> List[int]:

    le = len(l)

    if d == 1:
        diag = [l[i][i] for i in range(len(l))]
    elif d == 2:
        diag = [l[i][j] for i, j in zip(range(le), reversed(range(le)))]
    else:
        raise ValueError(f'wrong diag param {d}')
    return sum(diag)


def score(oldval: int, newval: int) -> int:
    return abs(oldval - newval)


def wrong_sums(l: Matrix) -> Tuple[List, List, bool, bool]:
    """Returns the idx of every axis in a tuple
    tuple[0]: list 
        idx of wrong sums in axis 0 (rows)
    tuple[1]: list
        idx of wrong sums in axis 1 (columns)
    tuple[2]: bool
        if primary diagonal is dif to constant
    tuple[3]: bool
        if second diagonal is dif to constant
    """

    const = magic_constant(len(l))
    axis0 = [i for i, e in enumerate(sum_ax(l, 0)) if e != const]
    axis1 = [i for i, e in enumerate(sum_ax(l, 1)) if e != const]
    diag1 = sum_diagonal(l, 1) != const
    diag2 = sum_diagonal(l, 2) != const

    return (axis0, axis1, diag1, diag2)


def magic_constant(n: int) -> int:
    return n*((n**2 + 1) / 2)


# --------------------
#  The func to submit
# --------------------


def formingMagicSquare(s: Matrix) -> int:
    """Given a square, returns the minimum number of changes
    ti transform the square into a magic square
    """

    assert isinstance(s, list)
