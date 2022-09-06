import math

import Utilities.DataProcess

data = Utilities.DataProcess.split_data_to_int("AOC_7_input.txt", ",")


def add_to(target) -> int:
    return sum([x for x in range(1, target + 1)])


data.sort()
target = data[0]
final = (target, math.inf)
for i in range(len(data) - 1):
    _fuels = [add_to(abs(i - x)) for x in data]
    fuel = sum(_fuels)
    if fuel < final[1]:
        final = (i, fuel)
print(final)
