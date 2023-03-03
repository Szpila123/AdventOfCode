elf_cals = []
with open('input.txt') as file:
    cals = 0
    for line in file:
        if line != '\n':
            cals += int(line)
        else:
            elf_cals.append(cals)
            cals = 0

print(max(elf_cals))
print(sum(sorted(elf_cals, reverse=True)[:3]))
