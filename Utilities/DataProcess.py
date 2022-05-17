def GetVerticalDataToListStr(_path):
    with open(file = _path) as f:
        data = f.read().split("\n")
    return data

def GetVerticalDataToListInt(_path):
    with open(file = _path) as f:
        _data = f.read().split("\n")
        data = [eval(x) for x in _data]
    return data

def SplitData(_path, symbol):
    with open(file=_path) as f:
        _data = f.read().split(symbol)
    return _data

def SplitDataToInt(_path, symbol):
    with open(file=_path) as f:
        _data = f.read().split(symbol)
        data = [eval(x) for x in _data]
    return data