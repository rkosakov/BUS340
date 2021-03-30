number = input('Enter a number between 0 and 1000: ')
sum = 0

while number != '':
    digit = int(number[len(number) - 1])
    sum += digit
    number = number[:-1]

print(f'The sum of the digits is: {sum}')

