from time import time

import numpy as np


def solve_bn(low, high, ax, ay, bx, by, prizex, prizey):
    # check if increasing bn increases or decreases output in binary search
    machine_type = 1
    if (ay * ((prizex - (bx * 20)) / ax)) + (by * 20) > (ay * ((prizex - (bx * 80)) / ax)) + (by * 80):
        machine_type = 2
    while high >= low:
        mid = (high + low) // 2

        success, direction = check_bn(ax, ay, bx, by, prizex, prizey, mid, machine_type)
        if success:
            return mid

        # if too many button presses
        if direction == 'High':
            high = mid - 1
        else:
            low = mid + 1

    # no solution found
    return -1


def check_bn(ax, ay, bx, by, prizex, prizey, bn, machine_type):
    # bn correct
    if (ay * ((prizex - (bx * bn)) / ax)) + (by * bn) == prizey:
        return True, None
    # check if we're high or low
    if (ay * ((prizex - (bx * bn)) / ax)) + (by * bn) > prizey:
        if machine_type == 1:
            return False, 'High'
        else:
            return False, 'Low'
    else:
        if machine_type == 1:
            return False, 'Low'
        else:
            return False, 'High'


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
        ax, ay = machine['A']
        bx, by = machine['B']
        prizex, prizey = machine['Prize']

        # an = number of A button presses
        # bn = number of B button presses
        # linear equations substitution
        # (ax * an) + (bx * bn) = prizex
        # (ay * an) + (by * bn) = prizey

        # (ax * an) = prizex - (bx * bn)
        # an = (prizex - (bx * bn)) / ax

        # (ay * ((prizex - (bx * bn)) / ax)) + (by * bn) = prizey

        # binary search for bn
        low = 0
        high = 100
        bn = solve_bn(low, high, ax, ay, bx, by, prizex, prizey)

        if bn == -1:
            print(f'Machine {machine}')
            print('No solution')
            continue

        an = (prizex - (bx * bn)) / ax

        tokens_total += 3 * an + bn
        print(f'Machine {machine}')
        print(f'an = {an}, bn = {bn}')

    print(f'Token total = {tokens_total}')


if __name__ == '__main__':
    start_time = time()
    main()
    print('\nProcess complete')
    print(f"Process time: {round(time() - start_time, 2)} seconds.")
