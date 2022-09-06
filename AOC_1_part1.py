from Utilities.DataProcess import get_vertical_data_to_list_str as d_p

data = d_p("AOC_1_input.txt")

ammount = 0
for i in range(1, len(data)):
    current = eval(data[i])
    previous = eval(data[i-1])
    if current > previous:
        ammount += 1
print(ammount)


