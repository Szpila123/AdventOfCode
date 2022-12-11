import re
from copy import deepcopy

text = """
D     NF 
HF   LJH 
RH   FVGH
ZQ  ZWLJB
SWH BHDCM
PRSGJJWZV
WBVFGTTTP
QVCHPQZDW
"""

columns = [[x for x in col if not x.isspace()] for col in zip(*text.strip().split('\n'))]
columns_2 = deepcopy(columns)

with open('input.txt') as file:
    for line in file:
        if 'move' in line:
            count, col_from, col_to = [int(x) for x in re.findall(r'\d+', line)]
            col_from -= 1
            col_to -= 1

            columns[col_to] = columns[col_from][count-1::-1] + columns[col_to]
            columns[col_from] = columns[col_from][count:]

            columns_2[col_to] = columns_2[col_from][:count] + columns_2[col_to]
            columns_2[col_from] = columns_2[col_from][count:]

print(''.join([column[0] for column in columns]))
print(''.join([column[0] for column in columns_2]))
