from typing import Counter


NUMBER_OF_ELEMENTS = 5
number = []
sum = 0
counter = 0

for i in range(NUMBER_OF_ELEMENTS):
    value = eval(input('Enter a new number: '))
    number.append(value)
    sum += value

average = sum / NUMBER_OF_ELEMENTS
for i in range(NUMBER_OF_ELEMENTS):
    if number[i] > average:
        counter += 1

print('Average is ', average)
print('Number of elements above the average: ', counter)