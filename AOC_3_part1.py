from Utilities.DataProcess import get_vertical_data_to_list_str as d_p
data = d_p("AOC_3_input.txt")

gamma = ['0b']
epsilon = ['0b']

for i in range(12):
    _l = [x[i] for x in data]
    if _l.count("1") > len(_l)/2 :
        gamma.append("1")
        epsilon.append("0")
    else:
        gamma.append("0")
        epsilon.append("1")
print(gamma)
g = (eval("".join(gamma)))
print(epsilon)
e = (eval("".join(epsilon)))
print(g*e)