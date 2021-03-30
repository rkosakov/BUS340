import random

rand_number = random.randint(100, 999)

number = eval(input('Enter your lottery pick (three digits): '))

if  number <= 99 or number >= 1000: 
    print('The number is invalid')


rand_number_in_str = str(rand_number) 
# rand_num_digit1 = int(rand_number_in_str[0])
# rand_num_digit2 = int(rand_number_in_str[1])
# rand_num_digit3 = int(rand_number_in_str[2])

number_in_str = str(number)
# num_digit1 = int(number_in_str[0])
# num_digit2 = int(number_in_str[1])
# num_digit3 = int(number_in_str[2])


matchedDigits = 0


# if (rand_num_digit1 == num_digit1):
#     matchedDigits += 1
# if (rand_num_digit1 == num_digit2):
#     matchedDigits += 1
# if (rand_num_digit1 == num_digit3):
#     matchedDigits += 1
# if (rand_num_digit2 == num_digit2):
#     matchedDigits += 1
# if (rand_num_digit2 == num_digit3):
#     matchedDigits += 1
# if (rand_num_digit3 == num_digit3):
#     matchedDigits += 1



print(f'The lottery number is {rand_number}')

if rand_number == number:
    print('Match all digit: you win $10,000')
elif matchedDigits == 3:
    print('Match all digits: you win $5,000')
elif matchedDigits == 2:
    print('Match two digits: you win $3,000')
else:
    print('Sorry, no match')


