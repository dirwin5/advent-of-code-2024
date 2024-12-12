from time import time

import numpy as np


def process_stone(value: int) -> np.ndarray:
    if value == 0:
        return np.array([1])
    n_digits = int(np.log10(value)) + 1
    # even number of digits
    if n_digits % 2 == 0:
        # split without string conversion
        # calculate N for splitting into 2 parts
        N = 10 ** (n_digits // 2)
        v1 = value // N
        v2 = value % N
        return np.array([v1, v2])

    return np.array([value * 2024])


def main():
    with open('input.txt', 'r') as f:
        line = f.read().strip()

    stones = np.array(line.split()).astype(int)

    # create dict. key = stone value, value = how many stones with that value
    stones_dict = {}
    for stone in stones:
        stone_count = stones_dict.get(stone, 0)
        stone_count += 1
        stones_dict[stone] = stone_count

    # iterate 75 times
    for i in range(75):
        stones_dict_updated = {}
        for stone_value, stone_count in stones_dict.items():
            stone_values_updated = process_stone(stone_value)
            for stone_value_updated in stone_values_updated:
                stone_count_updated = stones_dict_updated.get(stone_value_updated, 0)
                stone_count_updated += 1 * stone_count
                stones_dict_updated[stone_value_updated] = stone_count_updated

        stones_dict = stones_dict_updated.copy()

    stones_total = 0
    for stone_count in stones_dict.values():
        stones_total += stone_count

    print(f'Stones = {stones_total}')


if __name__ == '__main__':
    start_time = time()
    main()
    print('\nProcess complete')
    print(f"Process time: {round(time() - start_time, 2)} seconds.")
