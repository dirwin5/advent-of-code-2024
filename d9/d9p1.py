from time import time

import numpy as np


def main():
    with open('input.txt', 'r') as f:
        line = f.read().strip()

    disk_map = np.array(list(line)).astype(int)

    files = disk_map[0::2]
    spaces = disk_map[1::2]
    ids = np.array(np.arange(len(files)))

    # how many blocks will be used
    file_blocks_total = files.sum()

    checksum = 0
    block_i = 0
    file_i = 0
    file_end_i = -1
    file_n = files[file_i]
    file_end_n = files[file_end_i]
    space_i = 0
    space_n = 0
    while block_i < file_blocks_total:
        if file_n > 0:
            checksum += ids[file_i] * block_i
            file_n -= 1
            if file_n == 0:
                space_n = spaces[space_i]
                file_i += 1
        elif space_n > 0:
            checksum += ids[file_end_i] * block_i
            space_n -= 1
            file_end_n -= 1
            if space_n == 0:
                file_n = files[file_i]
                space_i += 1
            if file_end_n == 0:
                file_end_i -= 1
                file_end_n = files[file_end_i]
        # zero length space
        else:
            file_n = files[file_i]
            space_i += 1
            # don't increment block index in this case
            continue

        block_i += 1

    print(f'Checksum = {checksum}')


if __name__ == '__main__':
    start_time = time()
    main()
    print('\nProcess complete')
    print(f"Process time: {round(time() - start_time, 2)} seconds.")
