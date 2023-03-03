import re
from ast import Call
from typing import Callable


class Monkey():
    def __init__(self, items: list[int], operation: Callable[[int], int], test: Callable[[int], int]) -> None:
        self._start_itmes = items.copy()
        self.items = items
        self.operation = operation
        self.test = test
        self.inspection_cnt = 0

    def do_turn(self, relief=True) -> list[tuple[int, int]]:
        self.inspection_cnt += len(self.items)
        thrown_items = list(map(lambda x: self.operation(x)//(3 if relief else 1), self.items))
        self.items = []
        return [(item, self.test(item)) for item in thrown_items]

    def add_item(self, item: int) -> None:
        self.items.append(item)

    def reset(self) -> None:
        self.items = self._start_itmes.copy()
        self.inspection_cnt = 0


def create_monkey_from_text(lines: list[str]) -> Monkey:
    items = [int(x) for x in re.findall(r'\d+', lines[1])]

    if lines[2].split()[5].isnumeric():
        oper_number = int(lines[2].split()[5])
        def oper(x): return x * oper_number if '*' in lines[2] else x + oper_number
    else:
        def oper(x): return x * x if '*' in lines[2] else x + x

    throw_to = [int(line.split()[5]) for line in lines[4:6]]
    div_number = int(lines[3].split()[3])
    def test(x): return throw_to[0] if not x % div_number else throw_to[1]

    return Monkey(items, oper, test)


monkeys = []
lcm_divs = 1
with open('input.txt') as file:
    content = file.readlines()
    for lines in [[line.strip() for line in content[i:i+7]] for i in range(0, len(content), 7)]:
        monkeys.append(create_monkey_from_text(lines))
        lcm_divs *= int(lines[3].split()[3])

for _ in range(20):
    for monkey in monkeys:
        thrown = monkey.do_turn()
        for item, to in thrown:
            monkeys[to].add_item(item)
print(sorted([monkey.inspection_cnt for monkey in monkeys], reverse=True)[:2])

for monkey in monkeys:
    monkey.reset()
for cnt in range(10000):
    for monkey in monkeys:
        thrown = monkey.do_turn(relief=False)
        for item, to in thrown:
            monkeys[to].add_item(item % lcm_divs)
print(sorted([monkey.inspection_cnt for monkey in monkeys], reverse=True)[:2])
