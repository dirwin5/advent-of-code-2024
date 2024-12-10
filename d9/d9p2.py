from time import time

import numpy as np


def find_runs(x):
    """
    Function credit alimanfoo - https://gist.github.com/alimanfoo/c5977e87111abe8127453b21204c1065
    Find runs of consecutive items in an array.
    """

    # ensure array
    x = np.asanyarray(x)
    if x.ndim != 1:
        raise ValueError('only 1D array supported')
    n = x.shape[0]

    # handle empty array
    if n == 0:
        return np.array([]), np.array([]), np.array([])

    else:
        # find run starts
        loc_run_start = np.empty(n, dtype=bool)
        loc_run_start[0] = True
        np.not_equal(x[:-1], x[1:], out=loc_run_start[1:])
        run_starts = np.nonzero(loc_run_start)[0]

        # find run values
        run_values = x[loc_run_start]

        # find run lengths
        run_lengths = np.diff(np.append(run_starts, n))

        return run_values, run_starts, run_lengths


def main():
    with open('input.txt', 'r') as f:
        line = f.read().strip()

    disk_map = np.array(list(line)).astype(int)

    files = disk_map[0::2]
    ids = np.arange(len(files))

    # make dict. key = id and value = file size
    id_dict = {}
    for id, file_size in zip(ids, files):
        id_dict[id] = file_size

    # build array. gaps are -1
    space = False
    arr = np.array([])
    id = 0
    for item in disk_map:
        if space:
            arr = np.append(arr, [-1] * item)
            space = False
        else:
            arr = np.append(arr, [id] * item)
            id += 1
            space = True

    run_values, run_starts, run_lengths = find_runs(arr)

    # keep only spaces
    mask = run_values == -1
    # space_values = run_values[mask]
    space_starts = run_starts[mask]
    space_lengths = run_lengths[mask]

    for i in np.arange(max(ids), min(ids) - 1, -1):
        file_size = id_dict[i]
        if file_size > space_lengths.max():
            continue
        space_i = np.argmax(space_lengths >= file_size)
        space_start = space_starts[space_i]
        id_start = np.argmax(arr == i)
        if id_start > space_start:
            arr[space_start:space_start + file_size] = i
            arr[id_start:id_start + file_size] = -1
            run_values, run_starts, run_lengths = find_runs(arr)
            mask = run_values == -1
            space_starts = run_starts[mask]
            space_lengths = run_lengths[mask]

    # remove -1 values for checksum
    arr[arr < 0] = 0
    checksum_arr = arr * np.arange(len(arr))
    checksum = checksum_arr.sum()

    print(f'Checksum = {checksum}')


if __name__ == '__main__':
    start_time = time()
    main()
    print('\nProcess complete')
    print(f"Process time: {round(time() - start_time, 2)} seconds.")
