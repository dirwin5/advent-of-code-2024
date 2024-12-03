from time import time


def check_levels(levels: list[int], min_inc: int=1, max_inc: int=3) -> bool:
    # find direction between first 2 values
    start_ascending = True
    if levels[0] > levels[1]:
        start_ascending = False

    safe = True
    for i, level in enumerate(levels):
        if i == len(levels) - 1:
            continue
        diff = level - levels[i + 1]
        # check if difference is out of safe range
        if abs(diff) < min_inc or abs(diff) > max_inc:
            safe = False
            break
        # check direction matches direction of first 2 values
        ascending = True
        if diff > 0:
            ascending = False
        if ascending != start_ascending:
            safe = False
            break

    return safe


def main():
    with open('input.txt', 'r') as f:
        reports = f.read().splitlines()

    min_inc = 1
    max_inc = 3

    safe_reports = 0
    for report in reports:
        levels_str = report.split()
        levels = [int(level) for level in levels_str]

        # check if full report is safe
        safe = check_levels(levels, min_inc, max_inc)

        # if not, check all iterations of list with 1 item removed
        if not safe:
            for i, level in enumerate(levels):
                levels_copy = levels.copy()
                levels_copy.pop(i)
                safe = check_levels(levels_copy, min_inc, max_inc)
                if safe:
                    break

        if safe:
            safe_reports += 1

    print(f'Total safe reports = {safe_reports}')


if __name__ == '__main__':
    start_time = time()
    main()
    print('\nProcess complete')
    print(f"Process time: {round(time() - start_time, 2)} seconds.")
