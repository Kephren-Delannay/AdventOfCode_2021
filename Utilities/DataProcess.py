def get_vertical_data_to_list_str(_path):
    with open(file=_path) as f:
        data = f.read().split("\n")
    return data


def get_vertical_data_to_list_int(_path):
    with open(file=_path) as f:
        _data = f.read().split("\n")
        data = [eval(x) for x in _data]
    return data


def split_data(_path, symbol):
    with open(file=_path) as f:
        _data = f.read().split(symbol)
    return _data


def split_data_to_int(_path, symbol):
    with open(file=_path) as f:
        _data = f.read().split(symbol)
        data = [eval(x) for x in _data]
    return data


def get_vertical_data_to_2d_array(_path):
    with open(file=_path) as f:
        _data = f.read().split("\n")
        data = [list(x) for x in _data]
    return data
