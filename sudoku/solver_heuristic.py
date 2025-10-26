# sudoku/solver_heuristic.py

from sudoku.grid import Sudoku

def find_best_cell(sudoku: Sudoku):
    """
    Choisit la case vide ayant le moins de valeurs possibles (heuristique MRV).
    Cela réduit la taille de l’arbre de recherche.
    """
    best = None
    min_candidates = 10

    for i in range(9):
        for j in range(9):
            if sudoku.grid[i][j] == 0:
                candidates = [v for v in range(1, 10) if sudoku.is_valid(i, j, v)]
                if len(candidates) < min_candidates:
                    min_candidates = len(candidates)
                    best = (i, j, candidates)
    return best


def solve_heuristic(sudoku: Sudoku):
    """
    Variante du solveur utilisant MRV pour accélérer la recherche.
    """
    best = find_best_cell(sudoku)
    if not best:
        return True  # terminé

    i, j, candidates = best

    for val in candidates:
        sudoku.grid[i][j] = val
        if solve_heuristic(sudoku):
            return True
        sudoku.grid[i][j] = 0
    return False
