from Utilities.DataProcess import GetVerticalDataToListStr as d_p
data = d_p("AOC_2_input.txt")
test = data[1]

position = [0,0]

def process_input(_input):
    delta = (0,0)
    p = _input.split(" ")
    direction = p[0]
    ammount = p[1]
    if direction == "down":
        delta = (0, eval(ammount))
    elif direction == "up":
        delta = (0, eval(ammount) * -1)
    else:
        delta = (eval(ammount), 0)
    return delta

for instruction in data:
    delta = process_input(instruction)
    position[0] += delta[0]
    position[1] += delta[1]
print(position)
print(position[0]*position[1])
        