
number = eval(input('Enter an integer (0 to exit): '))
sum = 0
counter = 0
negative_counter = 0
positive_counter = 0

while number != 0:
    counter += 1
    sum += number
    if number > 0:
        positive_counter += 1
    else:
        negative_counter += 1
    number = eval(input('Enter an integer (0 to exit): '))

average = sum / counter
print(f'The average of the numbers is: {average:.2f}')
print(f'The number of positive number is: {positive_counter}')
print(f'The number of negative numbers is: {negative_counter}')