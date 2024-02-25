def solve_sudoku(grid):
    empty_cells = [(i, j) for i in range(9) for j in range(9) if grid[i][j] == 0]
    if not empty_cells:
        return True  # La grille est déjà résolue

    row, col = empty_cells[0]

    for num in range(1, 10):
        if all(num != grid[row][j] for j in range(9)) and \
           all(num != grid[i][col] for i in range(9)) and \
           all(num != grid[row//3*3 + i//3][col//3*3 + i%3] for i in range(9)):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0

    return False

def forward_checking(grid, empty_cells):
    for row, col in empty_cells:
        possible_values = set(range(1, 10))
        for i in range(9):
            possible_values.discard(grid[row][i])  # Éliminer les valeurs de la ligne
            possible_values.discard(grid[i][col])  # Éliminer les valeurs de la colonne
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                possible_values.discard(grid[i][j])  # Éliminer les valeurs de la sous-grille
        if not possible_values:
            return False
    return True

def solve_sudoku_with_forward_checking(grid):
    empty_cells = [(i, j) for i in range(9) for j in range(9) if grid[i][j] == 0]
    empty_cells.sort(key=lambda cell: len(set(range(1, 10)) - {grid[cell[0]][j] for j in range(9)} - {grid[i][cell[1]] for i in range(9)} - {grid[cell[0]//3*3 + i//3][cell[1]//3*3 + i%3] for i in range(9)}))
    if solve_sudoku(grid):
        return True
    if forward_checking(grid, empty_cells):
        return solve_sudoku(grid)
    return False

# Exemple d'utilisation :
# grid = [
#     [5, 3, 0, 0, 7, 0, 0, 0, 0],
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 9]
# ]
# if solve_sudoku_with_forward_checking(grid):
#     for row in grid:
#         print(row)
# else:
#     print("Aucune solution trouvée")
