import random 

# Step 1
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

# Step 2
if number1 < number2:
    number1, number2 = number2, number1

#Step 3
answer = eval(input(f'What is {number1} - {number2}? '))

if number1 - number2 == answer:
    print('You are correct')
else:
    print(f'Your answer is wrong.\n {number1} - {number2} is {number1 - number2}.')