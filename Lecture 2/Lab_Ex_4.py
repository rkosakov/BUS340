balance, interest_rate = eval(input('Enter the balance and interest rate (e.g., 3 for 3%): '))

interest = balance * ((interest_rate) / 1200)
print(f'The interest rate is {interest:.5f}')