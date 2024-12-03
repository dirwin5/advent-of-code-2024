from time import time
import re


def main():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()

    total = 0
    do = True
    for line in lines:
        instructions = re.findall("mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", line)
        for instruction in instructions:
            if instruction == "do()":
                do = True
                continue
            if instruction == "don't()":
                do = False
                continue
            if do:
                instruction = instruction.replace('mul(', '').replace(')', '')
                n1, n2 = instruction.split(',')
                total += int(n1) * int(n2)

    print(f'Total = {total}')


if __name__ == '__main__':
    start_time = time()
    main()
    print('\nProcess complete')
    print(f"Process time: {round(time() - start_time, 2)} seconds.")
