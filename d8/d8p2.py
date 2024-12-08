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
    if len(loc_arr) < 2:
        return []

    # find combinations
    antinodes = []
    for comb in combinations(loc_arr, 2):
        # add antenna locations
        antinodes.append(tuple(comb[0]))
        antinodes.append(tuple(comb[1]))
        # find horz and vert distance between points
        diff = comb[0] - comb[1]

        # find antinode locations
        # check if each antinode lies within grid
        # square grid so only need one dimension
        max_i, _ = grid.shape

        # direction 1
        antinode = comb[0]
        while True:
            antinode = antinode + diff
            if antinode.min() >= 0 and antinode.max() < max_i:
                antinodes.append(tuple(antinode))
            else:
                break
        # direction 2
        antinode = comb[1]
        while True:
            antinode = antinode - diff
            if antinode.min() >= 0 and antinode.max() < max_i:
                antinodes.append(tuple(antinode))
            else:
                break

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
