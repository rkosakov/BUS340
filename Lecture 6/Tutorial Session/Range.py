def printNums(upper, lower = 0, step = 0):
    if lower == 0 and step == 0:
        if upper != 0:
            for i in range(upper):
                print(i, ' ', end = '')
        else:
            print('The upper bound must be bigger than 0')
    elif step == 0:
        if lower < upper:
            for i in range(lower, upper):
                print(i, ' ', end = '')
        else:
            print('The lower bound must be smaller than the upper one!')
    else:
        if step < 0:
            if lower < upper:
                for i in range(lower, upper):
                    print(i, ' ', end = '')
            else:
                print('The lower bound must be smaller than the upper one!')

        elif step > 0:
            if lower < upper:
                for i in range(lower, upper, step):
                    print(i, ' ', end = '')
            else:
                 print("The Lower bound must be > Upper bound!")

def main():
    lowerBound = 0
    step = 0
    upperBound = eval(input('Enter an upper bound: '))

    inValue = input('Enter a lower bound: ')
    if inValue != '':
        lowerBound = int(inValue)
    inValue = input('Enter a step: ')
    if inValue != '':
        step = int(inValue)
    
    printNums(lowerBound, upperBound, step)

main()