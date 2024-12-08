from time import time
from itertools import repeat, combinations

import numpy as np


def find_antinodes(grid: np.ndarray,
                   value: str) -> list[tuple]:
    if value == '.':
        return []
    # find value locations
    i_arr, j_arr = np.where(grid == value)
    loc_arr = np.column_stack((i_arr, j_arr))

    # find combinations
    antinodes = []
    for comb in combinations(loc_arr, 2):
        # find horz and vert distance between points
        diff = comb[0] - comb[1]
        # find antinode locations
        antinode1 = comb[0] + diff
        antinode2 = comb[1] - diff
        # check if each antinode lies within grid
        # square grid so only need one dimension
        # convert to tuples as will need to be hashable later for removing duplicates
        max_i, _ = grid.shape
        if antinode1.min() >= 0 and antinode1.max() < max_i:
            antinodes.append(tuple(antinode1))
        if antinode2.min() >= 0 and antinode2.max() < max_i:
            antinodes.append(tuple(antinode2))

    return antinodes


def main():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()

    lines_arrays = []
    for line in lines:
        lines_arrays.append(list(line))

    grid = np.array(lines_arrays)

    unique_values, counts = np.unique(grid, return_counts=True)

    antinode_lists = map(find_antinodes, repeat(grid, len(unique_values)), unique_values)

    # create single list
    antinodes = []
    for antinode_list in antinode_lists:
        antinodes.extend(antinode_list)

    # remove duplicates
    antinodes = set(antinodes)

    total = len(antinodes)
    print(f'Total = {total}')


if __name__ == '__main__':
    start_time = time()
    main()
    print('\nProcess complete')
    print(f"Process time: {round(time() - start_time, 2)} seconds.")
