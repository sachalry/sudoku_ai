# sudoku/grid.py

class Sudoku:
    """
    Classe représentant une grille de Sudoku 9x9.
    0 représente une case vide.
    """

    def __init__(self, grid):
        # La grille est une liste de listes d'entiers (9x9)
        self.grid = grid

    # ---------------------
    # ACCÈS AUX ÉLÉMENTS
    # ---------------------

    def get_row(self, i):
        """Retourne la i-ème ligne de la grille."""
        return self.grid[i]

    def get_col(self, j):
        """Retourne la j-ème colonne de la grille."""
        return [self.grid[i][j] for i in range(9)]

    def get_block(self, i, j):
        """
        Retourne le bloc 3x3 contenant la case (i, j).
        Exemple : (4,5) appartient au bloc central (indices 3..5, 3..5)
        """
        bi, bj = 3 * (i // 3), 3 * (j // 3)
        return [
            self.grid[x][y]
            for x in range(bi, bi + 3)
            for y in range(bj, bj + 3)
        ]

    # ---------------------
    # VALIDATION & RECHERCHE
    # ---------------------

    def find_empty(self):
        """Retourne la position (i, j) d'une case vide, ou None si complet."""
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    return i, j
        return None

    def is_valid(self, i, j, val):
        """
        Vérifie si la valeur 'val' peut être placée en (i, j)
        sans violer les règles du sudoku.
        """
        if val in self.get_row(i): return False
        if val in self.get_col(j): return False
        if val in self.get_block(i, j): return False
        return True

    def display(self):
        """Affiche joliment la grille dans la console."""
        for i, row in enumerate(self.grid):
            if i % 3 == 0 and i != 0:
                print("-" * 21)
            for j, val in enumerate(row):
                if j % 3 == 0 and j != 0:
                    print("| ", end="")
                print(val if val != 0 else ".", end=" ")
            print()
