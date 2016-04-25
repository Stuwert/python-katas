def findNextSquare(sq):
    i = 1
    while i * i <= sq:
        i = i + 1
    else:
        if (i - 1) * (i - 1) == sq:
            return i * i
        else:
            return -1


print(findNextSquare(15))
