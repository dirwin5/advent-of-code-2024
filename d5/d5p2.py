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


def fix_order(update, rules):
    pages_to_check = update.copy()
    target_len = len(pages_to_check)
    fixed_update = []
    i = 0
    while len(fixed_update) < target_len:
        page = pages_to_check[i]
        us_rules = rules[page][0]
        matches = set(us_rules).intersection(pages_to_check)
        if len(matches) < 1:
            fixed_update.append(page)
            pages_to_check.pop(i)
            i = 0
        else:
            i += 1

    return fixed_update


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

    valid_total = 0
    invalid_total = 0
    for update in updates:
        valid = check_valid(update, rules)

        if valid:
            valid_total += update[int(len(update) / 2)]

        else:
            fixed_update = fix_order(update, rules)
            invalid_total += fixed_update[int(len(fixed_update) / 2)]

    print(f'valid_total = {valid_total}')
    print(f'invalid_total = {invalid_total}')


if __name__ == '__main__':
    start_time = time()
    main()
    print('\nProcess complete')
    print(f"Process time: {round(time() - start_time, 2)} seconds.")
