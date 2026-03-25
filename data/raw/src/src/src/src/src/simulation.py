import numpy as np
import matplotlib.pyplot as plt

def simulate_fire(grid_size=20, steps=10):
    grid = np.zeros((grid_size, grid_size))

    grid[grid_size//2][grid_size//2] = 1

    for _ in range(steps):
        new_grid = grid.copy()
        for i in range(grid_size):
            for j in range(grid_size):
                if grid[i][j] == 1:
                    for x in range(max(0, i-1), min(grid_size, i+2)):
                        for y in range(max(0, j-1), min(grid_size, j+2)):
                            if grid[x][y] == 0:
                                new_grid[x][y] = 1
        grid = new_grid

    plt.imshow(grid, cmap='hot')
    plt.title("Fire Spread Simulation")
    plt.show()
