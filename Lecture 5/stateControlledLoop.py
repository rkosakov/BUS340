done = False

while not done:
    num = int(input('Enter the numberic grade: '))
    if num >= 0 and num <= 100:
        done = True
    else:
        print('Error: grade must be between 100 and 0')

print(f'The grade is: {num}')
