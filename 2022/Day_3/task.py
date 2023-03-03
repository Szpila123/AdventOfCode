def get_item_prio(item: str):
    if item == '\n':
        return 0
    recom = - ord('a') + 1 if 'a' <= item <= 'z' else - ord('A') + 27
    return ord(item) + recom


sum_prio, sum_badges = 0, 0
with open('input.txt') as file:
    lines = file.readlines()
    for line in lines:
        sum_prio += get_item_prio((set(line[len(line)//2:]) & set(line[:len(line)//2])).pop())

    for i in range(0, len(lines), 3):
        sum_badges += sum(get_item_prio(item) for item in set(lines[i]) & set(lines[i+1]) & set(lines[i+2]))

print(sum_prio)
print(sum_badges)
