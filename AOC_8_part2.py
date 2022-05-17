with open(file="AOC_8_input.txt") as f:
    _data = f.read().split('\n')
    data = [x.split(" | ") for x in _data]


def contains(_a, _b):
    for i in range(len(_b)):
        if _b[i] not in _a:
            return False
    if i == len(_b) - 1:
        return True


def identify(_inputs, _outputs):
    combination = {}
    for el in _inputs:
        if len(el) == 2:
            combination['1'] = el
        elif len(el) == 4:
            combination['4'] = el
        elif len(el) == 3:
            combination['7'] = el
        elif len(el) == 7:
            combination['8'] = el
    five = [x for x in _inputs if len(x) == 5]
    six = [x for x in _inputs if len(x) == 6]
    # Find the 9
    for el in six:
        if contains(list(el), list(combination['4'])):
            combination['9'] = el
            break
    # Find the 3
    for el in five:
        if contains(list(el), list(combination['1'])):
            combination['3'] = el
            break
    # Find the 5
    for el in five:
        if contains(list(combination['9']), list(el)) and el != combination['3']:
            combination['5'] = el
            break
    # Find the 6
    for el in six:
        if contains(list(el), list(combination['5'])) and el != combination['9']:
            combination['6'] = el
            break
    # Deduce the 0 and 2
    values = [combination[k] for k in combination]
    for el in five:
        if el not in values:
            combination['2'] = el
            break
    for el in six:
        if el not in values:
            combination['0'] = el
            break
    return combination


def get_keys_from_value(d, val):
    return [k for k, v in d.items() if v == val]


def compare(_a, _b):
    if len(_a) != len(_b):
        return False
    for i in range(len(_b)):
        if _b[i] not in _a:
            return False
    return True


results = []
for entry in data:
    inputs = entry[0].split(' ')
    outputs = entry[1].split(' ')
    _combinations = identify(inputs, outputs)
    result = []
    for el in outputs:
        _el = list(el)
        for i in range(10):
            if compare(_el, list(_combinations[str(i)])):
                result.append(str(i))
                break
    results.append(int(''.join(result)))
print(results)
print(sum(results))