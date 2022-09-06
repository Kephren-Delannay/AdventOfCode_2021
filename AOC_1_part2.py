from Utilities.DataProcess import get_vertical_data_to_list_int as d_p

data = d_p("AOC_1_input.txt")

def create_window(start_index):
    window_total = sum(data[start_index:start_index+3])
    return window_total

s = 0
previous = None
times = 0

while s < len(data) - 2: 
    window = create_window(s)
    if previous != None:
        if window > previous : 
            times += 1        
    s += 1
    previous = window

print(times)
