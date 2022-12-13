CYCLES = list(range(20, 260, 40))
GRID_WIDTH = 40
GRID_HEIGHT = 6

signal_strength = 0
grid = [['.'] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
with open('input.txt') as file:
    cycles, register_value = 0, 1

    for line in file:
        line = line.split()

        duration = 1 if line[0] == 'noop' else 2
        value = int(line[1]) if len(line) == 2 else 0

        for _ in range(duration):
            if cycles + 1 in CYCLES:
                signal_strength += cycles * register_value
            if abs(register_value - cycles%GRID_WIDTH) <= 1:
                grid[cycles//GRID_WIDTH][cycles%GRID_WIDTH] = '#'
            cycles += 1

        register_value += value

print(signal_strength)
for line in grid:
    print(''.join(line))
