day = 0

q1 = 'Is your Birthday in Set 1?\n \
    1  3  5  7\n\
     9 11 13 15\n \
    17 19 21 23\n \
    25 27 29 31\n \
    \nEnter Yes or No: '
answer = input(q1)

if answer == 'Yes':
    day += 1

q2 = 'Is your Birthday in Set 2?\n \
    2  3  6  7\n \
    10 11 14 15\n \
    18 19 22 23\n \
    26 27 30 31\n \
    \nEnter Yes or No: '
answer = input(q2) 

if answer == 'Yes':
    day += 2

q3 = 'Is your Birthday in Set 3?\n \
     4  5  6  7\n \
    12 13 14 15\n \
    20 21 22 23\n \
    28 29 30 31\n \
    \nEnter Yes or No: '
answer = input(q3)

if answer == 'Yes':
    day += 4

q4 = 'Is your Birthday in Set 4?\n \
     8  9 10 11\n \
    12 13 14 15\n \
    24 25 26 27\n \
    28 29 30 31\n \
    \nEnter Yes or No: '
answer = input(q4)

if answer == 'Yes':
    day += 8

q5 = 'Is your Birthday in Set 5?\n \
    16 17 18 19\n \
    20 21 22 23\n \
    24 25 26 27\n \
    28 29 30 31\n \
    \nEnter Yes or No: '
answer = input(q5)

if answer == 'Yes':
    day += 16

print(f'\nYour birthday is: {day}!')