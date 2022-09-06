from Utilities.DataProcess import get_vertical_data_to_list_str as d_p
data = d_p("AOC_3_input.txt")

ox = data.copy()
co = data.copy()

i = 0
while len(ox) > 1 and i < 12:
    _l = [x[i] for x in ox]
    if _l.count("1") >= _l.count("0") :
        ox = [x for x in ox if x[i] == "1"]
    else:
        ox = [x for x in ox if x[i] == "0"]
    
    i += 1

i = 0
while len(co) > 1 and i < 12:
    _l = [x[i] for x in co]
    if _l.count("1") >= _l.count("0") :
        co = [x for x in co if x[i] == "0"]
    else:
        co = [x for x in co if x[i] == "1"]
    
    i += 1

print(ox)
print(co)

o = eval("0b" + "".join(ox))
c = eval("0b" + "".join(co))
print(o)
print(c)
print(o * c)