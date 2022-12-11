def get_marker(line: str, marker_len: int) -> int:
    count = [0] * (ord('z') - ord('a') + 1)
    singles = 0

    for signal in line[:marker_len]:
        count[ord(signal) - ord('a')] += 1
        match count[ord(signal) - ord('a')]:
            case 1:
                singles += 1
            case 2:
                singles -= 1

    idx = marker_len
    while singles != marker_len:
        new_signal = line[idx]
        count[ord(new_signal) - ord('a')] += 1
        match count[ord(new_signal) - ord('a')]:
            case 1:
                singles += 1
            case 2:
                singles -= 1

        old_signal = line[idx-marker_len]
        count[ord(old_signal) - ord('a')] -= 1
        match count[ord(old_signal) - ord('a')]:
            case 1:
                singles += 1
            case 0:
                singles -= 1
        idx += 1

    return idx


with open('input.txt') as file:
    line = file.readline()
    print(get_marker(line, 4))
    print(get_marker(line, 14))
