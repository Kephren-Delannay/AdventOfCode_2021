from Utilities.DataProcess import get_vertical_data_to_2d_array as spliter

data = spliter("AOC_9_input.txt")
low_points = []
for i in range(len(data)):
    for j in range(len(data[0])):
        _test = eval(data[i][j])
        # test the surroundings
        if j > 0:
            if eval(data[i][j-1]) < _test:
                continue
        if j < len(data[0]) - 1:
            if eval(data[i][j+1]) < _test:
                continue
        if i > 0:
            if eval(data[i-1][j]) < _test:
                continue
        if i < len(data) - 1:
            if eval(data[i+1][j]) < _test:
                continue
        low_points.append(eval(data[i][j]))

print(low_points)
risk = [x + 1 for x in low_points]
print(sum(risk))