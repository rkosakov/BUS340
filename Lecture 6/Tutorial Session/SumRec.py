def SumBetweenNumbers(lower, upper):
    
    if lower <= upper:
        sum += lower
        SumBetweenNumbers(lower + 1, upper)
    else:
        return sum

sum = SumBetweenNumbers(1,3)
print(sum)

