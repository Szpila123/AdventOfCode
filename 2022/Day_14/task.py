import re
from itertools import pairwise

START_POINT = (0, 500)


def fill_stones(grid: list[list[str]], coordinates: list[list[tuple[int, int]]]) -> None:
    for line in coordinates:
        for point_from, point_to in pairwise(line):
            diff = (point_to[0] - point_from[0], point_to[1] - point_from[1])
            dist = max([abs(val) for val in diff])
            diff = tuple(val//dist for val in diff)

            current = point_from
            for _ in range(dist + 1):
                grid[current[0]][current[1]] = '#'
                current = (current[0] + diff[0], current[1] + diff[1])


def simulate(grid: list[list[str]], start_point: tuple[int, int]) -> None:
    def next_move(point: tuple[int, int]) -> tuple[int, int]:
        if point[0] == len(grid) - 1 or grid[point[0]+1][point[1]] == '.':
            return (1, 0)
        elif point[1] == 0 or grid[point[0]+1][point[1]-1] == '.':
            return (1, -1)
        elif point[1] == len(grid[0]) or grid[point[0]+1][point[1]+1] == '.':
            return (1, 1)
        return (0, 0)

    def check_inbound(point: tuple[int, int]) -> bool:
        return point[0] >= 0 and point[1] >= 0 and point[0] < len(grid) and point[1] < len(grid[0])

    while True:
        current_point = start_point
        while (move := next_move(current_point)) != (0, 0):
            current_point = (current_point[0] + move[0], current_point[1] + move[1])
            if not check_inbound(current_point):
                return
        else:
            grid[current_point[0]][current_point[1]] = '+'
            if current_point == start_point:
                return


with open('input.txt') as file:
    coordinates = [[tuple(reversed([int(number) for number in coordinates.split(',')]))
                    for coordinates in re.findall(r'\d+,\d+', line)] for line in file.readlines()]
    minmax_y = [min([min([point[0] for point in line]) for line in coordinates]),
                max([max([point[0] for point in line]) for line in coordinates])]
    minmax_x = [min([min([point[1] for point in line]) for line in coordinates]),
                max([max([point[1] for point in line]) for line in coordinates])]

GUARD_FIRST = 20
grid_first = [['.'] * (minmax_x[1] - minmax_x[0] + 1) for _ in range(minmax_y[1] - minmax_y[0] + GUARD_FIRST + 1)]
coordinates_first = [[(point[0] - minmax_y[0] + GUARD_FIRST, point[1] - minmax_x[0])
                      for point in line] for line in coordinates]

fill_stones(grid_first, coordinates_first)
simulate(grid_first, (START_POINT[0], START_POINT[1] - minmax_x[0]))

count = sum([line.count('+') for line in grid_first])
print(count)

GUARD_SECOND = 300
BOTTOM_OFFSET = 2
grid_second = [['.'] * (minmax_x[1] - minmax_x[0] + GUARD_SECOND) for _ in range(minmax_y[1] + BOTTOM_OFFSET + 1)]
coordinates_second = [[(point[0], point[1] - minmax_x[0] + GUARD_SECOND//2) for point in line] for line in coordinates]
coordinates_second.append([(minmax_y[1] + BOTTOM_OFFSET, 0), (minmax_y[1] + BOTTOM_OFFSET, len(grid_second[0]) - 1)])

fill_stones(grid_second, coordinates_second)
simulate(grid_second, (START_POINT[0], START_POINT[1] - minmax_x[0] + GUARD_SECOND//2))

count = sum([line.count('+') for line in grid_second])
print(count)
