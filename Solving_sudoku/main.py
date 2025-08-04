def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else "." for num in row))


def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None


def is_valid(grid, num, pos):
    row, col = pos

    # Check row
    if num in grid[row]:
        return False

    # Check column
    for i in range(9):
        if grid[i][col] == num:
            return False

    # Check 3x3 box
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == num:
                return False

    return True


def solve(grid):
    find = find_empty(grid)
    if not find:
        return True
    row, col = find

    for num in range(1, 10):
        if is_valid(grid, num, (row, col)):
            grid[row][col] = num

            if solve(grid):
                return True

            grid[row][col] = 0

    return False


# ==== User Input Section ====
print("Enter your Sudoku puzzle row by row.")
print("Use 0 for empty cells. Each row must contain 9 digits without spaces.")
print("Example for a row: 530070000")

user_grid = []

for i in range(9):
    while True:
        row_input = input(f"Enter row {i+1}: ")
        if len(row_input) == 9 and row_input.isdigit():
            row = [int(ch) for ch in row_input]
            user_grid.append(row)
            break
        else:
            print("Invalid input. Please enter exactly 9 digits (0-9).")

print("\nOriginal Sudoku:")
print_grid(user_grid)

if solve(user_grid):
    print("\nSolved Sudoku:")
    print_grid(user_grid)
else:
    print("\nNo solution exists.")