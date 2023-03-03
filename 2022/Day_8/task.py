from copy import deepcopy

grid: list[list[int]] = []
with open('input.txt') as file:
    for line in file:
        grid.append([int(x) for x in line if x != '\n'])

max_grid_col = deepcopy(grid)
max_grid_row = deepcopy(grid)

for idx_y in range(1, len(grid)-1):
    for idx_x in range(1, len(grid[0])-1):
        max_grid_row[idx_y][idx_x] = max(grid[idx_y][idx_x-1], max_grid_row[idx_y][idx_x-1])
        max_grid_col[idx_y][idx_x] = max(grid[idx_y-1][idx_x], max_grid_col[idx_y-1][idx_x])

for idx_y in range(len(grid)-2, 0, -1):
    for idx_x in range(len(grid[0])-2, 0, -1):
        max_grid_row[idx_y][idx_x] = min(max_grid_row[idx_y][idx_x], max(
            max_grid_row[idx_y][idx_x+1], grid[idx_y][idx_x+1]))
        max_grid_col[idx_y][idx_x] = min(max_grid_col[idx_y][idx_x], max(
            grid[idx_y+1][idx_x], max_grid_col[idx_y+1][idx_x]))

count = 2 * len(grid) + 2*(len(grid[0])-2)
for idx_y in range(1, len(grid)-1):
    for idx_x in range(1, len(grid[0])-1):
        if grid[idx_y][idx_x] > min(max_grid_row[idx_y][idx_x], max_grid_col[idx_y][idx_x]):
            count += 1

print(count)


def count_shorter(idx_y: int, idx_x: int, grid: list[list[int]], grid_dir: list[list[int]], direction: tuple[int, int]):
    seen_trees = 1
    next_y, next_x = idx_y + direction[0], idx_x + direction[1]

    while grid[next_y][next_x] < grid[idx_y][idx_x] and next_y not in [0, len(grid)-1] and next_x not in [0, len(grid[0])-1]:
        seen_trees += grid_dir[next_y][next_x]
        next_y += direction[0] * grid_dir[next_y][next_x]
        next_x += direction[1] * grid_dir[next_y][next_x]

    return seen_trees


grid_left = deepcopy(grid)
grid_right = deepcopy(grid)
grid_up = deepcopy(grid)
grid_down = deepcopy(grid)

for idx_y in range(len(grid)):
    for idx_x in range(len(grid[0])):
        if idx_x == 0:
            grid_left[idx_y][idx_x] = 0
        else:
            grid_left[idx_y][idx_x] = count_shorter(idx_y, idx_x, grid, grid_left, (0, -1))

        if idx_y == 0:
            grid_up[idx_y][idx_x] = 0
        else:
            grid_up[idx_y][idx_x] = count_shorter(idx_y, idx_x, grid, grid_up, (-1, 0))

for idx_y in range(len(grid)-1, -1, -1):
    for idx_x in range(len(grid[0])-1, -1, -1):
        if idx_x == len(grid[0])-1:
            grid_right[idx_y][idx_x] = 0
        else:
            grid_right[idx_y][idx_x] = count_shorter(idx_y, idx_x, grid, grid_right, (0, 1))

        if idx_y == len(grid)-1:
            grid_down[idx_y][idx_x] = 0
        else:
            grid_down[idx_y][idx_x] = count_shorter(idx_y, idx_x, grid, grid_down, (1, 0))

max_visible = 0
for idx_y in range(0, len(grid)):
    for idx_x in range(0, len(grid[0])):
        new_amount = grid_down[idx_y][idx_x] * grid_up[idx_y][idx_x] * \
            grid_left[idx_y][idx_x] * grid_right[idx_y][idx_x]
        max_visible = max(max_visible, new_amount)

print(max_visible)
