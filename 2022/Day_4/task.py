import re

contained_cnt = 0
overlap_cnt = 0
with open('input.txt') as file:
    for line in file:
        numbers = [int(x) for x in re.findall(r'\d+', line)]
        if numbers[2] <= numbers[0] <= numbers[1] <= numbers[3] or numbers[0] <= numbers[2] <= numbers[3] <= numbers[1]:
            contained_cnt += 1
            overlap_cnt += 1
        elif numbers[2] <= numbers[0] <= numbers[3] or numbers[2] <= numbers[1] <= numbers[3]:
            overlap_cnt += 1

print(contained_cnt)
print(overlap_cnt)
