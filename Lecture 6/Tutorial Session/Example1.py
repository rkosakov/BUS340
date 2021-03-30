# def displayRange(lower, upper):
#     while lower < upper:
#         print(lower,' ', end = '')
#         lower += 1

def displayRangeRec(lower, upper):
    if lower <= upper:
        print(lower, ' ', end = '')
        displayRangeRec(lower + 1, upper)
        
displayRangeRec(1, 10)