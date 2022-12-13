from math import copysign

GRID_SIZE = 600
START_IDX = GRID_SIZE//2

TASK_1_NODES = 2
TASK_2_NODES = 10

MOVE_MAP = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (-1, 0),
    'D': (1, 0)
}


def knots_dist(x: list[int], y: list[int]) -> list[int]:
    return [x[0] - y[0], x[1] - y[1]]


def simulate_rope(knots_pos: list[list[int]], move: tuple[int, int]) -> None:
    knots_pos[0][0] += move[0]
    knots_pos[0][1] += move[1]

    if len(knots_pos) == 1 or move == [0, 0]:
        return

    next_move = (0, 0)
    match knots_dist(knots_pos[0], knots_pos[1]):
        case ([(2 | -2), 0] | [0, (2 | -2)]) as direction:
            next_move = (direction[0]//2, direction[1]//2)
        case ([(2 | -2), _] | [_, (2 | -2)]) as direction:
            next_move = (int(copysign(1, direction[0])), int(copysign(1, direction[1])))

    return simulate_rope(knots_pos[1:], next_move)


grid_first, grid_second = [[['.'] * GRID_SIZE for _ in range(GRID_SIZE)] for _ in range(2)]
grid_first[START_IDX][START_IDX] = '#'
grid_second[START_IDX][START_IDX] = '#'

with open('input.txt') as file:
    knots_first = [[START_IDX] * 2 for _ in range(TASK_1_NODES)]
    knots_second = [[START_IDX] * 2 for _ in range(TASK_2_NODES)]

    for line in file:
        move, times = line.split()
        times = int(times)
        move = MOVE_MAP[move]

        for _ in range(times):
            for knots, grid in zip([knots_first, knots_second], [grid_first, grid_second]):
                simulate_rope(knots, move)
                grid[knots[-1][0]][knots[-1][1]] = '#'

for count in [sum(row.count('#') for row in grid) for grid in [grid_first, grid_second]]:
    print(count)
