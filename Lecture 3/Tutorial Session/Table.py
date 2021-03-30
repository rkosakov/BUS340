import math

SEPARATOR = '|'
FORMAT_1 = '>5d'
FORMAT_2 = '<12.2f'
FORMAT_3 = '<10.2f'

print('---------------------------')
print(format('x', '>5s') + SEPARATOR, format('x^2', '12s'), format('Vx', '10s')) 
print('---------------------------')

x = 5
print(format(x, FORMAT_1) + SEPARATOR, format(x ** 2, FORMAT_2), format(math.sqrt(x), FORMAT_3))

x = 500
print(format(x, FORMAT_1) + SEPARATOR, format(x ** 2, FORMAT_2), format(math.sqrt(x), FORMAT_3))

x = 20
print(format(x, FORMAT_1) + SEPARATOR, format(x ** 2, FORMAT_2), format(math.sqrt(x), FORMAT_3))

x = 3000
print(format(x, FORMAT_1) + SEPARATOR, format(x ** 2, FORMAT_2), format(math.sqrt(x), FORMAT_3))