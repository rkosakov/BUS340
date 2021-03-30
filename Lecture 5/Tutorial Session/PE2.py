number_of_items = eval(input('Enter a number of items: '))

sum = 0

for i in range(0, number_of_items):
    items_price = eval(input('Enter the price of the item: '))
    sum += items_price

shipping_charge = 0

if number_of_items <= 3:
    shipping_charge = 3.50
elif number_of_items > 3 and number_of_items <= 7:
    shipping_charge = 5.00
elif number_of_items > 7 and number_of_items <= 11:
    shipping_charge = 7.00
elif number_of_items > 11 and number_of_items <= 16:
    shipping_charge = 9.00
else:
    shipping_charge = 10.00

tax_amount = 0.075 * sum

print('----------------------------------')
print('           Sales Receipt')
print(f'Total Purchases: ${sum:.2f}')
print(f'Sales Tax        ${tax_amount:.2f}')
print(f'Number of Items Purchased: {number_of_items}')
print(f'Shipping charge:  ${shipping_charge:.2f}  ')
print('----------------------------------')
print(f'Grand Total:     ${(sum + tax_amount + shipping_charge):.2f}')