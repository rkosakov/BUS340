number_of_lines = eval(input('Enter the number of lines: '))

for i in range(1, number_of_lines + 1):
    for j in range(number_of_lines, 1, -1):
        if j <= i:
            print(j, end = ' ')
        else:
            print(' ', end = ' ')
    for j in range(1, number_of_lines + 1):
        if j <= i:
            print(j, end = ' ')
        else:
            print(' ', end = ' ')
    print()