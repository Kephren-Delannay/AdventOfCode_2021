with open(file='AOC_11_input.txt') as f:
    _data = f.read().split('\n')
    data = [list(x) for x in _data]

import numpy as np
dt = np.array(data, dtype=int)


def get_neighbors(_dt, i, j, size):
    for k in range(max(0, i - 1), min(i + 1, size) + 1):
        for l in range(max(0, j - 1), min(j + 1, size) + 1):
            if i == k and j == l:
                continue
            dt[k, l] += 1


def simulate(_dt, _size):
    for i in range(_size):
        for j in range(_size):
            _dt[i, j] += 1
            if _dt[i, j] > 9:
                _dt[i, j] = 0
                get_neighbors(_dt, i, j, _size)
    print(_dt)


simulate(dt, 5)


