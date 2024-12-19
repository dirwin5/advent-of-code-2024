"""
Brute force method. Slow. Used this to help troubleshoot linear equations method
"""
from time import time

import numpy as np


def main():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()

    machines = []
    machine = {}
    for line in lines:
        if line.startswith('Button'):
            button = line.split(':')[0][-1:]
            machine[button] = (int(line.split('+')[1].split(',')[0]), int(line.split('+')[2]))
        if line.startswith('Prize'):
            machine['Prize'] = (int(line.split('=')[1].split(',')[0]), int(line.split('=')[2]))
            machines.append(machine)
            machine = {}

    tokens_total = 0
    for machine in machines:
        a = np.array(machine['A'])
        b = np.array(machine['B'])
        prize = np.array(machine['Prize'])

        print(f'Machine {machine}')
        solution = False
        for i in range(100):
            if solution:
                break
            for j in range(100):
                total = i * a + j * b
                if np.all(total == prize):
                    tokens_total += 3 * i + j
                    solution = True
                    print(f'an = {i}, bn = {j}')
                    break
                if np.any(total > prize):
                    break

        if not solution:
            print('No solution')

    print(f'Token total = {tokens_total}')


if __name__ == '__main__':
    start_time = time()
    main()
    print('\nProcess complete')
    print(f"Process time: {round(time() - start_time, 2)} seconds.")
