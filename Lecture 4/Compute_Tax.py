from sys import exit
status = input('Enter the Filing Status: ')
income = eval(input('Enter the Taxable Income: '))

tax = 0
if status == 'Single':
    if income <= 8350:
        tax = income * 0.10
    elif income >= 8351 and income <= 33950:
        tax = income * 0.15
    elif income >= 33951 and income <= 82250:
        tax = income * 0.25
    elif income >= 82250 and income <= 137050:
        tax = income * 0.28
    elif income >= 137051 and income <= 372950:
        tax = income * 0.33
    elif income >= 372951:
        tax = income * 0.35
elif status == 'Married Filing Jointly or Qualified Widow(er)':
    if income <= 1670:
        tax = income * 0.10
    elif income >= 16701 and income <= 67900:
        tax = income * 0.15
    elif income >= 67901 and income <= 137050:
        tax = income * 0.25
    elif income >= 137051 and income <= 208850:
        tax = income * 0.28
    elif income >= 208851 and income <= 373950:
        tax = income * 0.33
    elif income >= 372951:
        tax = income * 0.35
elif status == 'Married Filing Separately':
    if income <= 8350:
        tax = income * 0.10
    elif income >= 8351 and income <= 33950:
        tax = income * 0.15
    elif income >= 33951 and income <= 82250:
        tax = income * 0.25
    elif income >= 82250 and income <= 137050:
        tax = income * 0.28
    elif income >= 137051 and income <= 372950:
        tax = income * 0.33
    elif income >= 372951:
        tax = income * 0.35
elif status == 'Head of Household':
    if income <= 11950:
        tax = income * 0.10
    elif income >= 11951 and income <= 45500:
        tax = income * 0.15
    elif income >= 45501 and income <= 117450:
        tax = income * 0.25
    elif income >= 117451 and income <= 190200:
        tax = income * 0.28
    elif income >= 190201 and income <= 372950:
        tax = income * 0.33
    elif income >= 372951:
        tax = income * 0.35
    else:
        print('Invalid Status!')
        exit()

print(f'The tax is: {tax:.2f}')



