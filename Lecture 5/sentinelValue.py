data = eval(input('Enter an integer (the input ends if it is 0): '))

theSum = 0

while data != 0:
    theSum += data
    data = eval(input('Enter an integer (the input ends if it is 0): '))

print(f'The sum is: {theSum}')