match_results = {
    ('A', 'X'): 3 + 1,
    ('A', 'Y'): 6 + 2,
    ('A', 'Z'): 0 + 3,
    ('B', 'X'): 0 + 1,
    ('B', 'Y'): 3 + 2,
    ('B', 'Z'): 6 + 3,
    ('C', 'X'): 6 + 1,
    ('C', 'Y'): 0 + 2,
    ('C', 'Z'): 3 + 3
}

move_lookup = {
    ('A', 'X'): 'Z',
    ('A', 'Y'): 'X',
    ('A', 'Z'): 'Y',
    ('B', 'X'): 'X',
    ('B', 'Y'): 'Y',
    ('B', 'Z'): 'Z',
    ('C', 'X'): 'Y',
    ('C', 'Y'): 'Z',
    ('C', 'Z'): 'X'

}

sum_1, sum_2 = 0, 0
with open('input.txt') as file:
    for line in file:
        opponent, player = line.split()
        sum_1 += match_results[(opponent, player)]  # type: ignore
        sum_2 += match_results[(opponent, move_lookup[(opponent, player)])]  # type: ignore

print(sum_1)
print(sum_2)
