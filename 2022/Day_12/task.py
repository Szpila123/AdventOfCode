from collections import deque
from itertools import product


grid: list[list[int]]
with open('input.txt') as file:
    grid = [[ord(char) for char in line.strip()] for line in file.readlines()]
    pos_start = max([max([(idx_y, idx_x) if field == ord('S') else (-1, -1)
                    for idx_x, field in enumerate(row)]) for idx_y, row in enumerate(grid)])
    pos_end = max([max([(idx_y, idx_x) if field == ord('E') else (-1, -1)
                  for idx_x, field in enumerate(row)]) for idx_y, row in enumerate(grid)])

    grid[pos_start[0]][pos_start[1]] = ord('a')
    grid[pos_end[0]][pos_end[1]] = ord('z')

visited = set([pos_start])
to_visit: deque[tuple[tuple[int, int], int]] = deque([(pos_start, 0)])
grid_backtrace: list[list[tuple[tuple[int, int], int]]] = [[((-1, -1), -1)] * len(grid[0]) for _ in grid]

while len(to_visit) > 0 and to_visit[0][0] != pos_end:
    current = to_visit.popleft()
    current_pos, current_steps = current[0], current[1]
    for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        current_elevation = grid[current_pos[0]][current_pos[1]]
        next_y, next_x = current_pos[0] + y, current_pos[1] + x
        if 0 <= next_x < len(grid[0]) and 0 <= next_y < len(grid):
            next_elevation = grid[next_y][next_x]
            if next_elevation - current_elevation <= 1 and (next_y, next_x) not in visited:
                to_visit.append(((next_y, next_x), current_steps+1))
                visited.add((next_y, next_x))
                grid_backtrace[next_y][next_x] = ((current_pos[0], current_pos[1]), current_steps+1)

print(to_visit[0] if len(to_visit) > 0 else 'not found')

to_visit: deque[tuple[tuple[int, int], int]] = deque(
    [((y, x), 0) for y, x in product(range(len(grid)), range(len(grid[0]))) if grid[y][x] == ord('a')])

while len(to_visit) > 0:
    current = to_visit.popleft()
    current_pos, current_steps = current[0], current[1]
    for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        current_elevation = grid[current_pos[0]][current_pos[1]]
        next_y, next_x = current_pos[0] + y, current_pos[1] + x
        if 0 <= next_x < len(grid[0]) and 0 <= next_y < len(grid):
            next_elevation = grid[next_y][next_x]
            if next_elevation - current_elevation <= 1 and grid_backtrace[next_y][next_x][1] > current_steps + 1:
                to_visit.append(((next_y, next_x), current_steps+1))
                grid_backtrace[next_y][next_x] = ((current_pos[0], current_pos[1]), current_steps+1)

print(grid_backtrace[pos_end[0]][pos_end[1]])
