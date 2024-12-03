from time import time
import re


def main():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()

    total = 0
    for line in lines:
        instructions = re.findall('mul\(\d{1,3},\d{1,3}\)', line)
        for instruction in instructions:
            instruction = instruction.replace('mul(', '').replace(')', '')
            n1, n2 = instruction.split(',')
            total += int(n1) * int(n2)

    print(f'Total = {total}')


if __name__ == '__main__':
    start_time = time()
    main()
    print('\nProcess complete')
    print(f"Process time: {round(time() - start_time, 2)} seconds.")
