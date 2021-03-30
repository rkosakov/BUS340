def isEquilateral(a, b, c):
    if a == b:
        if a == c:
            if b == c:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def main():
    inValue = eval(input('Enter a side: '))
    if inValue > 0:
        a = inValue
    else:
        print('Enter a valid side')
        return
    
    inValue = eval(input('Enter a side: '))
    if inValue > 0:
        b = inValue
    else:
        print('Enter a valid side')
        return
    inValue = eval(input('Enter a side: '))
    if inValue > 0:
        c = inValue
    else:
        print('Enter a valid side')
        return

    check = isEquilateral(a, b, c)

    if check:
        print(f'A tiangle with sides {a}, {b}, {c} is equilateral!')
    else:
        print(f'A tiangle with sides {a}, {b}, {c} is not equilateral!')

main()