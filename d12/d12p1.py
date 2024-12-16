from time import time

import numpy as np


def get_adjacent_cells(current_loc: np.ndarray,
                       grid: np.ndarray
                       ) -> list[np.ndarray]:
    adjacent_cells = []
    directions = [np.array([0, 1]), np.array([1, 0]), np.array([0, -1]), np.array([-1, 0])]
    for direction in directions:
        target_loc = current_loc + direction
        # check target location lies within grid
        if target_loc.min() < 0 or target_loc[0] >= grid.shape[0] or target_loc[1] >= grid.shape[1]:
            continue
        adjacent_cells.append(target_loc)

    return adjacent_cells


def check_cell(target_loc: np.ndarray,
               grid: np.ndarray,
               target_value: str,
               cells_used_all: list[np.ndarray],
               cells_used_region: list[np.ndarray],
               area: int,
               perimeter: int) -> tuple[list[np.ndarray], int, int, list[np.ndarray], list[np.ndarray]]:
    # assuming target location lies within grid from check in get_adjacent_cells.
    adjacent_cells = []
    # check if this target loc has already been used in this region
    if np.any(np.all(target_loc == cells_used_region, axis=1)):
        return adjacent_cells, area, perimeter, cells_used_all, cells_used_region
    # check if this target loc has already been used for another region
    if np.any(np.all(target_loc == cells_used_all, axis=1)):
        perimeter += 1
        return adjacent_cells, area, perimeter, cells_used_all, cells_used_region
    # check if the target cell has the same value
    if grid[target_loc[0]][target_loc[1]] == target_value:
        cells_used_all.append(target_loc)
        cells_used_region.append(target_loc)
        adjacent_cells = get_adjacent_cells(target_loc, grid)
        area += 1
        # account for edge of grid perimeter
        perimeter += 4 - len(adjacent_cells)
    else:
        perimeter += 1

    return adjacent_cells, area, perimeter, cells_used_all, cells_used_region


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
            cells_used_all.append(current_loc)
            cells_used_region = [current_loc]
            cell_value = grid[i][j]
            area = 1
            perimeter = 0
            # look for adjacent cells of same value
            cells_to_check = get_adjacent_cells(current_loc, grid)
            # account for edge of grid perimeter
            perimeter += 4 - len(cells_to_check)
            while len(cells_to_check) > 0:
                cell_to_check = cells_to_check.pop()
                (adjacent_cells,
                 area,
                 perimeter,
                 cells_used_all,
                 cells_used_region) = check_cell(cell_to_check,
                                                 grid,
                                                 cell_value,
                                                 cells_used_all,
                                                 cells_used_region,
                                                 area,
                                                 perimeter)
                cells_to_check.extend(adjacent_cells)

            # print(f'Region complete. '
            #       f'Value: {cell_value}, Area: {area}, Perimeter: {perimeter}, Price: {area * perimeter}')
            price += area * perimeter

    print(f'Total price = {price}')


if __name__ == '__main__':
    start_time = time()
    main()
    print('\nProcess complete')
    print(f"Process time: {round(time() - start_time, 2)} seconds.")
