from time import time

import numpy as np


def process_stone(value: int) -> np.ndarray:
    if value == 0:
        return np.array([1])
    n_digits = int(np.log10(value)) + 1
    # even number of digits
    if n_digits % 2 == 0:
        v1 = int(str(value)[:n_digits // 2])
        v2 = int(str(value)[n_digits // 2:])
        return np.array([v1, v2])

    return np.array([value * 2024])


def main():
    with open('input.txt', 'r') as f:
        line = f.read().strip()

    stones = np.array(line.split()).astype(int)

    """ map takes around 0.5 seconds """
    for i in range(25):
        stones_updated = map(process_stone, stones)
        stones = np.concatenate(list(stones_updated))

    """ for loop around 13 times slower than map (6.4 seconds)"""
    # for i in range(25):
    #     stones_updated = np.array([], dtype=int)
    #     for stone in stones:
    #         stone_output = process_stone(stone)
    #         stones_updated = np.append(stones_updated, stone_output)
    #     stones = stones_updated.copy()
    #     print(f"Iteration {i+1} complete")

    print(f'Stone = {len(stones)}')


if __name__ == '__main__':
    start_time = time()
    main()
    print('\nProcess complete')
    print(f"Process time: {round(time() - start_time, 2)} seconds.")
