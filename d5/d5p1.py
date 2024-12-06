from time import time


def check_valid(update, rules):
    for i, page in enumerate(update):
        ds_pages = update[i + 1:]
        us_rules = rules[page][0]
        matches = set(ds_pages).intersection(us_rules)
        if len(matches) > 0:
            return False

    return True


def process_rule(rules, line):
    # process rule lines and add to rules dict
    v1, v2 = line.split('|')
    v1 = int(v1)
    v2 = int(v2)

    us, ds = rules.get(v1, ([], []))
    ds.append(v2)
    rules[v1] = (us, ds)

    us, ds = rules.get(v2, ([], []))
    us.append(v1)
    rules[v2] = (us, ds)

    return rules


def main():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()

    # rules dict. key = page no. value = ([us pages], [ds pages])
    rules = {}
    updates = []
    section1 = True
    for line in lines:
        # check for end of first input section
        if line == '':
            section1 = False
            continue
        if section1:
            rules = process_rule(rules, line)
        else:
            update_str = line.split(',')
            update = [int(page) for page in update_str]
            updates.append(update)

    total = 0
    for update in updates:
        valid = check_valid(update, rules)

        if valid:
            total += update[int(len(update) / 2)]

    print(f'Total = {total}')


if __name__ == '__main__':
    start_time = time()
    main()
    print('\nProcess complete')
    print(f"Process time: {round(time() - start_time, 2)} seconds.")
