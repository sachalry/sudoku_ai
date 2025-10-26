# sudoku/utils.py

def load_grid_from_file(path):
    """
    Charge un fichier texte de sudoku :
    - 9 lignes
    - 9 chiffres par ligne (0 pour vide)
    """
    grid = []
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                grid.append([int(x) for x in line])
    return grid


def save_grid_to_file(grid, path):
    """Sauvegarde la grille résolue dans un fichier texte."""
    with open(path, "w") as f:
        for row in grid:
            f.write("".join(str(x) for x in row) + "\n")
