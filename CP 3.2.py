def takeSecond(elem):
    return elem[1]
LIST = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

LIST.sort(key=takeSecond)

print('Sorted list:', LIST)
