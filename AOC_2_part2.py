from Utilities.DataProcess import GetVerticalDataToListStr as d_p
data = d_p("AOC_2_input.txt")
test = data[1]

position = [0,0]
aim = 0

def process_input(_input):
    global aim
    delta = (0,0)
    p = _input.split(" ")
    direction = p[0]
    ammount = p[1]
    if direction == "down":
        aim = aim + eval(ammount)
    elif direction == "up":
        aim = aim - eval(ammount)
    else:
        delta = (eval(ammount), aim * eval(ammount))
    return delta

for instruction in data:
    delta = process_input(instruction)
    position[0] += delta[0]
    position[1] += delta[1]
print(position)
print(position[0]*position[1])