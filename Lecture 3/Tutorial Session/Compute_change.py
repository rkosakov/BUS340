amount = eval(input('Enter an amount in double, e.g. 11.56: '))

remainingAmount = int(amount * 100)

numberOfTheDollars = remainingAmount // 100
remainingAmount = remainingAmount % 100

numberOfQuarters = remainingAmount // 25
remainingAmount = remainingAmount % 25

numberOfDimes = remainingAmount // 10
remainingAmount = remainingAmount % 10

numberOfNickels = remainingAmount // 5
remainingAmount = remainingAmount % 5

numberOfPenies = remainingAmount 

print('Your amount ', amount, 'consists of\n', \
    '\t', numberOfTheDollars, 'dollars\n',\
    '\t', numberOfQuarters, 'quarters\n', \
    '\t', numberOfDimes, 'dimes\n',\
    '\t', numberOfNickels, 'nickels\n',\
    '\t', numberOfPenies, 'pennies')
