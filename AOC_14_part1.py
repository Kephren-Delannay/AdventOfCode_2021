def create_rules_dict(rules):
    result = {}
    for element in rules:
        _el = element.split('->')
        _index = _el[0]
        _value = _el[1]
        result[_index] = _value
        return result

with open(file="AOC_14_input.txt") as f:
    data = f.read().split('\n')
    model = data[0]
    rules = [x for x in data[2::]]
    r = create_rules_dict(rules)
    print(r)

