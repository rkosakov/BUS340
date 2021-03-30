amount = eval(input('Loan Amount: $'))
years = eval(input('Number of Years: '))

print('\n{0:17}{1:19}{2}\n'.format('Interest Amount', 'Monthly Payment', 'Total Payment34'))

for i in range(25):
    yearlyRate = (5 + i * 0.125) / 100
    mothlyRate = yearlyRate / 12
    monthlyPayment = amount * mothlyRate / (1 - 1 / (1 + mothlyRate) ** (years * 12))
    totalPayment = monthlyPayment * 12 * years
    print('{0:<17.3%}${1:<18.2f}${2:<0.2f}'.format(yearlyRate, monthlyPayment, totalPayment))