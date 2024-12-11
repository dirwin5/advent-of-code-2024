from time import time

import numpy as np


def get_adjacent_cells(current_loc: np.ndarray,
                       grid: np.ndarray,
                       target_value: int,
                       cells_used: list[np.ndarray]) -> list[tuple[np.ndarray, int]]:
    adjacent_cells = []
    directions = [np.array([0, 1]), np.array([1, 0]), np.array([0, -1]), np.array([-1, 0])]
    for direction in directions:
        target_loc = current_loc + direction
        # check if this target loc has already been used
        # if np.any(np.all(target_loc == cells_used, axis=1)):
        #     continue
        # check target location lies within grid
        if target_loc.min() >= 0 and target_loc[0] < grid.shape[0] and target_loc[1] < grid.shape[1]:
            adjacent_cells.append((target_loc, target_value))

    return adjacent_cells


def main():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()

    lines_arrays = []
    for line in lines:
        lines_arrays.append(list(line))

    grid = np.array(lines_arrays).astype(int)

    # find 0 locations. i = vert. j = horz. top left = 0, 0
    i_arr, j_arr = np.where(grid == 0)
    zero_arr = np.column_stack((i_arr, j_arr))

    trailheads_score = 0
    for zero_loc in zero_arr:
        trailhead_score = 0
        target_value = 1
        # cells to check list. contains tuples in form (np.ndarray[i, j], target_value)
        cells_used = [zero_loc]
        cells_to_check = get_adjacent_cells(zero_loc, grid, target_value, cells_used)

        while len(cells_to_check) > 0:
            current_loc, target = cells_to_check.pop()
            # check if we've already used this cell
            # if np.any(np.all(current_loc == cells_used, axis=1)):
            #     continue
            # if the cell we're checking has the target value we need
            if grid[current_loc[0]][current_loc[1]] == target:
                cells_used.append(current_loc)
                if target == 9:
                    # as far as we can go on this route
                    trailheads_score += 1
                    continue
                # find next adjacent cells to be checked and add them to cells_to_check
                adjacent_cells = get_adjacent_cells(current_loc, grid, target + 1, cells_used)
                cells_to_check.extend(adjacent_cells)

    print(f'Total = {trailheads_score}')


if __name__ == '__main__':
    start_time = time()
    main()
    print('\nProcess complete')
    print(f"Process time: {round(time() - start_time, 2)} seconds.")
