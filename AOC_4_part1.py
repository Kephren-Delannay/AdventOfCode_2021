from Utilities.DataProcess import SplitData as spliter

data = spliter('AOC_4_input.txt', '*')
hands = data[0]
__boards = data[1]

numbers_drawn = [eval(x) for x in hands.split(',')]

#Process boards to create lists
_boards = __boards.split('\n\n')
boards = []
for b in _boards:
    _b = b.split('\n')
    _board = []
    for el in _b:
        _board.append(el.split(' '))
    boards.append(_board)
print(boards[0])