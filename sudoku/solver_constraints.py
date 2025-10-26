# sudoku/solver_constraints.py

from sudoku.grid import Sudoku

def init_domains(sudoku: Sudoku):
    """
    Initialise les domaines de chaque case (les valeurs possibles).
    Chaque domaine est un ensemble {1..9} sauf si la case est déjà remplie.
    """
    domains = [[set(range(1, 10)) for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if sudoku.grid[i][j] != 0:
                domains[i][j] = {sudoku.grid[i][j]}
    return domains


def eliminate(sudoku: Sudoku, domains, i, j, val):
    """
    Supprime 'val' des domaines des cases voisines (même ligne, colonne, bloc).
    """
    for x in range(9):
        if x != j:
            domains[i][x].discard(val)
        if x != i:
            domains[x][j].discard(val)

    bi, bj = 3 * (i // 3), 3 * (j // 3)
    for x in range(bi, bi + 3):
        for y in range(bj, bj + 3):
            if (x, y) != (i, j):
                domains[x][y].discard(val)


def forward_checking(sudoku: Sudoku, domains):
    """
    Implémente la propagation simple : lorsqu’une case est fixée, on
    élimine sa valeur des voisins. Si une case devient sans domaine → échec.
    """
    changed = True
    while changed:
        changed = False
        for i in range(9):
            for j in range(9):
                if sudoku.grid[i][j] == 0 and len(domains[i][j]) == 1:
                    val = next(iter(domains[i][j]))
                    sudoku.grid[i][j] = val
                    eliminate(sudoku, domains, i, j, val)
                    changed = True
    return True


def solve_constraints(sudoku: Sudoku):
    """
    Combine backtracking + propagation de contraintes.
    """
    domains = init_domains(sudoku)
    forward_checking(sudoku, domains)

    empty = sudoku.find_empty()
    if not empty:
        return True

    i, j = empty
    for val in sorted(domains[i][j]):
        if sudoku.is_valid(i, j, val):
            sudoku.grid[i][j] = val
            if solve_constraints(sudoku):
                return True
            sudoku.grid[i][j] = 0
    return False
