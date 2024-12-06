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


def find_next_location(cell_location, direction_i, directions):
    next_x = cell_location[0] + directions[direction_i][0]
    next_y = cell_location[1] + directions[direction_i][1]

    return next_x, next_y


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

    # direction list corresponding to up, right, down, left. 90 degree right turn each time
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    max_direction_i = 3

    # follow path and record where we've been. Without modification first to find cells which may affect the outcome
    start_location = (start_x, start_y)
    location = start_location
    direction_i = 0
    visited_cells = [(location, direction_i)]
    while True:
        edge, location, direction_i = find_next_cell(cells,
                                                     location,
                                                     direction_i,
                                                     max_direction_i,
                                                     directions,
                                                     max_x,
                                                     max_y)
        # check if we've been at this cell travelling in the same direction before
        if edge:
            break
        visited_cells.append((location, direction_i))

    # remove last visited cell as this is at the edge
    visited_cells.pop()

    loops = 0
    i = 0
    # try putting an obstacle in front of every position in the normal path
    # but only if we haven't already tested putting an obstacle at that cell
    tested_obstacle_locations = []
    for cell_location, direction_i in visited_cells:
        next_location = find_next_location(cell_location, direction_i, directions)
        # check if next location is already an obstruction
        while cells[next_location] == '#':
            # turn right
            direction_i += 1
            if direction_i > max_direction_i:
                direction_i = 0
            next_location = find_next_location(cell_location, direction_i, directions)

        # add new obstruction
        if next_location in tested_obstacle_locations:
            i += 1
            continue
        tested_obstacle_locations.append(next_location)
        cells_modified = cells.copy()
        cells_modified[next_location] = '#'

        # test path in modified map. start at new obstruction
        location = cell_location
        visited_cells_modified = [(location, direction_i)]
        while True:
            edge, location, direction_i = find_next_cell(cells_modified,
                                                         location,
                                                         direction_i,
                                                         max_direction_i,
                                                         directions,
                                                         max_x,
                                                         max_y)
            # check if we've been at this cell travelling in the same direction before
            if edge:
                break
            if (location, direction_i) in visited_cells_modified:
                loops += 1
                break
            visited_cells_modified.append((location, direction_i))

        i += 1
        if i % 100 == 0:
            print(f'cell {i} of {len(visited_cells)} complete')

    print(f'Total loops = {loops}')


if __name__ == '__main__':
    start_time = time()
    main()
    print('\nProcess complete')
    print(f"Process time: {round(time() - start_time, 2)} seconds.")
