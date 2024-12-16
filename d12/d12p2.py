from time import time

import numpy as np


def check_cell(current_loc: np.ndarray,
               grid: np.ndarray,
               cell_value: str,
               cells_used_all: list[np.ndarray],
               region_cells: list[np.ndarray],
               cells_to_check: list[np.ndarray],
               corners: int) -> tuple[list[np.ndarray], int, list[np.ndarray], list[np.ndarray]]:
    cells_used_all.append(current_loc)
    region_cells.append(current_loc)

    directions = [np.array([0, 1]),
                  np.array([1, 1]),
                  np.array([1, 0]),
                  np.array([1, -1]),
                  np.array([0, -1]),
                  np.array([-1, -1]),
                  np.array([-1, 0]),
                  np.array([-1, 1])]

    values = []

    for i, direction in enumerate(directions):
        target_loc = current_loc + direction
        # check target location lies within grid
        if target_loc.min() < 0 or target_loc[0] >= grid.shape[0] or target_loc[1] >= grid.shape[1]:
            values.append('OB')
        else:
            # if not a diagonal, check if the target cell has the same value
            if i % 2 == 0 and grid[target_loc[0]][target_loc[1]] == cell_value:
                # if this target loc hasn't already been used in this region,
                # and isn't already in the list for checking, add it to cells to check
                if not np.any(np.all(target_loc == region_cells, axis=1)):
                    if len(cells_to_check) == 0 or not np.any(np.all(target_loc == cells_to_check, axis=1)):
                        cells_to_check.append(target_loc)
            values.append(grid[target_loc[0]][target_loc[1]])

    corners += count_corners(values, cell_value)

    return cells_to_check, corners, cells_used_all, region_cells


def count_corners(values: list[str],
                  cell_value: str):
    corners = 0
    for i in [0, 2, 4, 6]:
        if values[i] != cell_value and values[i - 6] != cell_value:
            corners += 1
        if values[i] == cell_value and values[i - 6] == cell_value and values[i - 7] != cell_value:
            corners += 1

    return corners


def main():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()

    lines_arrays = []
    for line in lines:
        lines_arrays.append(list(line))

    # i = vert. j = horz. top left = 0, 0
    grid = np.array(lines_arrays)

    cells_used_all = []
    price = 0
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            current_loc = np.array([i, j])
            # check if cell has already been used
            if len(cells_used_all) > 0:
                if np.any(np.all(current_loc == cells_used_all, axis=1)):
                    continue
            # must be a new region. add current_loc to cells_used lists and get cell value
            cells_to_check = [current_loc]
            region_cells = []
            cell_value = grid[i][j]
            # no of corners == no of sides
            corners = 0

            while len(cells_to_check) > 0:
                cell_loc = cells_to_check.pop()
                cells_to_check, corners, cells_used_all, region_cells = check_cell(cell_loc,
                                                                                   grid,
                                                                                   cell_value,
                                                                                   cells_used_all,
                                                                                   region_cells,
                                                                                   cells_to_check,
                                                                                   corners)

            print(f'Region complete. '
                  f'Value: {cell_value}, Area: {len(region_cells)}, Sides: {corners}, Price: {len(region_cells) * corners}')
            price += len(region_cells) * corners

    print(f'Total price = {price}')


if __name__ == '__main__':
    start_time = time()
    main()
    print('\nProcess complete')
    print(f"Process time: {round(time() - start_time, 2)} seconds.")
