# sudoku/solver_backtrack.py

from sudoku.grid import Sudoku

def solve_backtracking(sudoku: Sudoku):
    """
    Résout un sudoku à l’aide de l’algorithme de backtracking.
    - Cherche une case vide
    - Tente les valeurs 1..9
    - Si valide, poursuit récursivement
    - Sinon, revient en arrière
    """
    empty = sudoku.find_empty()

    # Base : plus de case vide → le sudoku est résolu
    if not empty:
        return True

    i, j = empty

    for val in range(1, 10):
        if sudoku.is_valid(i, j, val):
            sudoku.grid[i][j] = val  # tentative
            if solve_backtracking(sudoku):
                return True
            sudoku.grid[i][j] = 0  # backtrack (échec)
    return False
