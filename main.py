# main.py

from sudoku.grid import Sudoku
from sudoku.solver_backtrack import solve_backtracking
from sudoku.solver_heuristic import solve_heuristic
from sudoku.solver_constraints import solve_constraints
from sudoku.utils import *
import time

if __name__ == "__main__":
    # Exemple de grille avec zéros (cases vides)
    grid = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
    ]

    # sudoku = Sudoku(grid)

    # print("Grille initiale :")
    # sudoku.display()

    # print("\nRésolution en cours (algorithme : backtracking)...")
    # if solve_backtracking(sudoku):
    #     print("\n✅ Sudoku résolu :")
    #     sudoku.display()
    # else:
    #     print("❌ Aucune solution trouvée.")

    # ➕ Tu peux tester les autres versions :
    # solve_heuristic(sudoku)
    # solve_constraints(sudoku)

    # ouvrir le fichier hard.txt et charger la grille

    grille = load_grid_from_file("examples/hard.txt")
    sudoku_fichier = Sudoku(grille)

    print("Grille initiale (depuis fichier) :")
    sudoku_fichier.display()
    print("\nRésolution en cours (algorithme : backtracking)...")
    time_ = time.time()
    if solve_backtracking(sudoku_fichier):
        print("\n✅ Sudoku résolu :")
        sudoku_fichier.display()
        # sauvegarder la grille résolue dans un fichier
        save_grid_to_file(sudoku_fichier.grid, "examples/hard_solved.txt")
        print(f"Temps de résolution : {time.time() - time_:.4f} secondes")
    else:
        print("❌ Aucune solution trouvée.")
