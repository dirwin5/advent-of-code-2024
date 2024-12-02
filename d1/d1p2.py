from time import time


def main():
    l1 = []
    l2 = []
    with open('input.txt', 'r') as f:
        for line in f:
            line_items = line.split()
            l1.append(int(line_items[0]))
            l2.append(int(line_items[1]))

    l1.sort()
    l2.sort()

    score = 0
    for id1 in l1:
        score += id1 * l2.count(id1)

    print(f'Total score = {score}')


if __name__ == '__main__':
    start_time = time()
    main()
    print('\nProcess complete')
    print(f"Process time: {round(time() - start_time, 2)} seconds.")
