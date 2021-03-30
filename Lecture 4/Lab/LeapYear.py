year = eval(input('Enter an year: '))

if year >= 1000:
    if year % 4 == 0 and year % 100 != 0:
        print(f'{year} is a Leap Year')
    else:
        print(f'{year} is not a Leap Year')
else:
    print('Invalid Year!')
