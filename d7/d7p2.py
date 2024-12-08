from time import time
from itertools import product
import operator


def main():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()

    # makes list of equations. tuple in format (expected, numbers)
    equations = []
    for line in lines:
        expected = int(line.split(':')[0])
        numbers_str = line.split(':')[1].strip().split()
        numbers = [int(number) for number in numbers_str]
        equations.append((expected, numbers))

    # define operator strings
    ops = {"+": operator.add, "*": operator.mul, "|": operator.concat}

    # check each equation. If it can be valid using + and * operators
    total = 0
    i = 0
    for expected, numbers in equations:
        # find all combination of operators
        combinations = product('+*|', repeat=len(numbers) - 1)
        for combination in combinations:
            # result = numbers[0]
            result = 0
            for j, number in enumerate(numbers):
                if j == 0:
                    result = number
                else:
                    if combination[j-1] == '|':
                        result = int(ops[combination[j - 1]](str(result), str(number)))
                    else:
                        result = ops[combination[j-1]](result, number)
                if result > expected:
                    break
            if result == expected:
                total += expected
                break

        i += 1
        if i % 100 == 0:
            print(f'Equation {i} of {len(equations)} complete')

    print(f'Total = {total}')


if __name__ == '__main__':
    start_time = time()
    main()
    print('\nProcess complete')
    print(f"Process time: {round(time() - start_time, 2)} seconds.")
