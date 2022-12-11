from typing import Callable


def deep_get(keys: list[str], dir: dict) -> dict:
    cur_dir = dir
    for key in keys:
        cur_dir = cur_dir[key]
    return cur_dir


def init_sizes(fs: dict) -> int:
    if fs['.type'] == 'dir':
        for name, item in fs.items():
            if name not in ['.size', '.type']:
                fs['.size'] += init_sizes(item)
    return fs['.size']


def fs_accumulate(fs: dict, f: Callable[[dict], int], accum_op: Callable[[int, int], int] = lambda x, y: x+y, accum_val: int = 0) -> int:
    accum = accum_val
    for name, value in fs.items():
        if name not in ['.size', '.type']:
            accum = accum_op(accum, fs_accumulate(value, f, accum_op, accum_val))
    return accum_op(accum, f(fs))


fs = {'.type': 'dir', '.size': 0}
with open('input.txt') as file:
    cur_path = []
    for line in file:
        commands = line.split()

        if commands[0] == '$' and commands[1] == 'cd':
            path = list(filter(lambda x: x != '', commands[2].split('/')))

            if commands[2][0] == '/':
                cur_path = path
                continue

            for token in path:
                if token == '..':
                    cur_path = cur_path[:-1]
                else:
                    cur_path.append(token)

        elif commands[0] == 'dir':
            cur_dir = deep_get(cur_path, fs)
            cur_dir[commands[1]] = {'.size': 0, '.type': 'dir'}
        elif commands[0].isnumeric():
            cur_dir = deep_get(cur_path, fs)
            cur_dir[commands[1]] = {'.size': int(commands[0]), '.type': 'file'}

init_sizes(fs)
print(fs_accumulate(fs, lambda x: x['.size'] if x['.type'] == 'dir' and x['.size'] <= 100000 else 0))

MAX_SIZE = 70000000
REQ_SIZE = 30000000
space_left = MAX_SIZE - fs['.size']
to_remove = REQ_SIZE - space_left
print(fs_accumulate(fs, lambda x: x['.size'] if x['.type'] ==
      'dir' and x['.size'] >= to_remove else MAX_SIZE, lambda x, y: min(x, y), MAX_SIZE))
