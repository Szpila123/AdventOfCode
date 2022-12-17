import json
from functools import cmp_to_key


Packet = list["Packet"] | int

SPECIAL_PACKETS: list[Packet] = [[[2]], [[6]]]


def compare_dsignal(left: Packet, right: Packet) -> int:
    match (isinstance(left, list), isinstance(right, list)):
        case True, True:
            for item_left, item_right in zip(left, right):  # type: ignore
                if (result := compare_dsignal(item_left, item_right)) in [-1, 1]:
                    return result
            if len(left) < len(right):  # type: ignore
                return -1
            elif len(left) > len(right):  # type: ignore
                return 1
            return 0

        case True, False:
            return compare_dsignal(left, [right])

        case False, True:
            return compare_dsignal([left], right)

        case False, False:
            if left < right:  # type: ignore
                return -1
            elif left > right:  # type: ignore
                return 1
            return 0
    return -2


good_idxs: list[int] = []
packets: list[Packet] = []
with open('input.txt') as file:
    lines = list(filter(lambda x: x != '\n', file.readlines()))
    for idx, (left, right) in enumerate([(json.loads(lines[i]), json.loads(lines[i+1])) for i in range(0, len(lines), 2)]):
        packets += [left, right]
        if compare_dsignal(left, right) == -1:
            good_idxs.append(idx + 1)

print(sum(good_idxs))

packets += SPECIAL_PACKETS
packets.sort(key=cmp_to_key(compare_dsignal))

indexes = [packets.index(packet) + 1 for packet in SPECIAL_PACKETS]
print(indexes[0] * indexes[1])
