import time
import os
import random

WIDTH = 30
HEIGHT = 20

# Create random starting grid
grid = [[random.choice([0, 1]) for _ in range(WIDTH)] for _ in range(HEIGHT)]


def count_neighbors(grid, row, col):
    count = 0

    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue

            r = row + dr
            c = col + dc

            if 0 <= r < HEIGHT and 0 <= c < WIDTH:
                count += grid[r][c]

    return count


def next_generation(grid):
    new_grid = [[0] * WIDTH for _ in range(HEIGHT)]

    for row in range(HEIGHT):
        for col in range(WIDTH):
            neighbors = count_neighbors(grid, row, col)

            if grid[row][col] == 1:
                if neighbors in (2, 3):
                    new_grid[row][col] = 1
            else:
                if neighbors == 3:
                    new_grid[row][col] = 1

    return new_grid


def display(grid):
    os.system("cls" if os.name == "nt" else "clear")

    for row in grid:
        print("".join("█" if cell else " " for cell in row))


while True:
    display(grid)

    new_grid = next_generation(grid)

    if new_grid == grid:
        print("\nSimulation stopped: stable state reached.")
        break

    grid = new_grid
    time.sleep(0.2)