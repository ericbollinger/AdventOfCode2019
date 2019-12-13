import sys, os
sys.path.append(os.path.relpath("../lib"))
from reader import read_lines

from math import floor

lines = read_lines("input.txt")
sum = 0
for item in lines:
    tmp = int(item)
    tmp = floor(tmp / 3)
    tmp -= 2
    sum += tmp

print(int(sum))
