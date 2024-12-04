from time import time


def find_word(letters, word, start_x, start_y, dx, dy, max_x, max_y):
    x = start_x
    y = start_y
    for letter in word[1:]:
        x += dx
        y += dy
        if x < 0 or x > max_x:
            return False
        if y < 0 or y > max_y:
            return False
        if letters[(x, y)] != letter:
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
    directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    word = 'XMAS'
    for (x, y), letter in letters.items():
        if letter != 'X':
            continue
        for (dx, dy) in directions:
            result = find_word(letters, word, x, y, dx, dy, max_x, max_y)
            if result:
                total += 1

    print(f'Total = {total}')


if __name__ == '__main__':
    start_time = time()
    main()
    print('\nProcess complete')
    print(f"Process time: {round(time() - start_time, 2)} seconds.")