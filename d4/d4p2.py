from time import time


def check_diags(letters, required_letters, start_x, start_y, diag, max_x, max_y):
    found_letters = ''
    for (dx, dy) in diag:
        x = start_x + dx
        y = start_y + dy
        if x < 0 or x > max_x:
            return False
        if y < 0 or y > max_y:
            return False
        if letters[(x, y)] not in required_letters:
            return False
        found_letters += letters[(x, y)]

    if found_letters not in [required_letters, required_letters[::-1]]:
        return False

    return True


def main():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()

    # create dict with key (x, y) and value letter. top left corner is (0, 0)
    letters = {}
    max_x = len(lines[0]) - 1
    max_y = len(lines) - 1
    for y, line in enumerate(lines):
        for x, letter in enumerate(line):
            letters[(x, y)] = letter

    # iterate over every letter
    total = 0
    diag1 = [(1, 1), (-1, -1)]
    diag2 = [(1, -1), (-1, 1)]
    required_letters = 'MS'
    for (x, y), letter in letters.items():
        if letter != 'A':
            continue
        # check both diagonals
        result1 = check_diags(letters, required_letters, x, y, diag1, max_x, max_y)
        if not result1:
            continue
        result2 = check_diags(letters, required_letters, x, y, diag2, max_x, max_y)
        if result2:
            total += 1

    print(f'Total = {total}')


if __name__ == '__main__':
    start_time = time()
    main()
    print('\nProcess complete')
    print(f"Process time: {round(time() - start_time, 2)} seconds.")