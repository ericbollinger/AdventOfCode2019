import sys, os
sys.path.append(os.path.relpath("../lib"))
from reader import read_lines

from math import floor

lines = read_lines("input.txt")
sum = 0
for n in lines:
    cur = int(n)
    while (cur > 0):
        cur = floor(cur/3) - 2
        if (cur > 0):
            sum += cur

print(int(sum))
