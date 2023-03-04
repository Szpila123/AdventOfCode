from copy import copy
import re


def analyze_row(sensors, becons, row):
    covered_sections: list[tuple[int, int]] = []
    for sensor, becon in zip(sensors, becons):
        row_dist = abs(sensor[1] - row)
        becon_dist = abs(sensor[0] - becon[0]) + abs(sensor[1] - becon[1])
        subsection_len = becon_dist - row_dist
        if subsection_len >= 0:
            covered_sections.append((sensor[0] - subsection_len, sensor[0] + subsection_len))

    covered_sections.sort()
    unique_covered_sections = [list(covered_sections[0])]
    for section in covered_sections[1:]:
        if section[0] <= unique_covered_sections[-1][1]:
            if section[1] > unique_covered_sections[-1][1]:
                unique_covered_sections[-1][1] = section[1]
        else:
            unique_covered_sections.append(list(section))

    return unique_covered_sections


ROW = 2000000
REG_PATTERN = r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)'
REG_GROUPS = 4
REG_EXPR = re.compile(REG_PATTERN)

sensors: list[list[int]] = []
becons: list[list[int]] = []

with open('input.txt') as file:
    for line in file:
        sensor_x, sensor_y, becon_x, becon_y = [int(num) for num in REG_EXPR.match(line).group(*range(1, REG_GROUPS+1))]
        sensors.append((sensor_x, sensor_y))
        becons.append((becon_x, becon_y))

unique_covered_sections = analyze_row(sensors, becons, ROW)
print(sum([section[1] - section[0] for section in unique_covered_sections]))

DISTRESS_MIN = 0
DISTRESS_MAX = 4000000
TUNING_MULT = 4000000

for row_idx in range(DISTRESS_MIN, DISTRESS_MAX):
    unique_covered_sections = analyze_row(sensors, becons, row_idx)
    if unique_covered_sections[0][0] > DISTRESS_MIN or unique_covered_sections[0][1] < DISTRESS_MAX:
        col_idx = unique_covered_sections[0][1] + 1
        break

print(col_idx * TUNING_MULT + row_idx)
