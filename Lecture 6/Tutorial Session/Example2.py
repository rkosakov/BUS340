def summation(lower, upper):
    if lower > upper:
        return 0
    else:
        print(lower)
        return lower + summation(lower + 1, upper)


summation(1, 5)