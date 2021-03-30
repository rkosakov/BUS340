number = eval(input('Enter a number between 1 and 9: '))

while not(number >= 1 and number <= 9):
      number = eval(input('Enter a number between 1 and 9: '))

for i in range(1, 10):
    print(f'{i} x {number} = {i * number}')