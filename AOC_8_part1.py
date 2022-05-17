with open(file="AOC_8_input.txt") as f:
    _data = f.read().split("\n")
    data = [x.split(" | ") for x in _data]

outputs = [x[1].split(' ') for x in data]
c = 0
for output in outputs:
    for el in output:
        #print(str(el) + " : " + str(len(el)))
        if len(el) == 2 or len(el) == 4 or len(el) == 3 or len(el) == 7:
            c += 1
print(c)