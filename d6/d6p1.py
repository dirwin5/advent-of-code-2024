from time import time


def find_next_cell(cells, current_location, direction_i, max_direction_i, directions, max_x, max_y):
    next_cell = '#'
    while next_cell == '#':
        next_x = current_location[0] + directions[direction_i][0]
        next_y = current_location[1] + directions[direction_i][1]
        # check if we're at an edge
        if next_x < 0 or next_x > max_x or next_y < 0 or next_y > max_y:
            edge = True
            return edge, current_location, direction_i
        # find value of next cell
        next_cell = cells[(next_x, next_y)]
        if next_cell == '#':
            # turn right
            direction_i += 1
            if direction_i > max_direction_i:
                direction_i = 0

    edge = False
    location = (next_x, next_y)

    return edge, location, direction_i


def main():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()

    # create dict with key (x, y) and value. top left corner is (0, 0). Also find start location
    cells = {}
    max_x = len(lines[0]) - 1
    max_y = len(lines) - 1
    start_x = None
    start_y = None
    for y, line in enumerate(lines):
        for x, value in enumerate(line):
            cells[(x, y)] = value
            if value == '^':
                start_x = x
                start_y = y

    # follow path and record where we've been
    # direction list corresponding to up, right, down, left. 90 degree right turn each time
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    direction_i = 0
    max_direction_i = 3
    location = (start_x, start_y)
    visited_cells = [location]
    edge = False
    while edge is False:
        edge, location, direction_i = find_next_cell(cells,
                                                     location,
                                                     direction_i,
                                                     max_direction_i,
                                                     directions,
                                                     max_x,
                                                     max_y)
        visited_cells.append(location)

    visited_cells_unique = set(visited_cells)

    print(f'Total = {len(visited_cells_unique)}')


if __name__ == '__main__':
    start_time = time()
    main()
    print('\nProcess complete')
    print(f"Process time: {round(time() - start_time, 2)} seconds.")
