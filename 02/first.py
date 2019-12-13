import sys, os
sys.path.append(os.path.relpath("../lib"))
from reader import read_lists

stream = read_lists("input.txt", ",")
stream = [int(x) for x in stream[0]]

stream[1] = 12
stream[2] = 2

for i in range(0, len(stream), 4):
    if stream[i] == 99:
        break

    idx1 = stream[i+1]
    idx2 = stream[i+2]
    idx3 = stream[i+3]

    if stream[i] == 1:
        stream[idx3] = stream[idx1] + stream[idx2]
    elif stream[i] == 2:
        stream[idx3] = stream[idx1] * stream[idx2]

print(",".join(str(x) for x in stream))
