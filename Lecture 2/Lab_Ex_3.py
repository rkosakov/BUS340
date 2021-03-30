water_in_kilograms = float(input('Enter the amount of water in kilograms: '))
initial_temperature = float(input('Enter the initial temperature: '))
final_temperature = float(input('Enter the temperature: '))

energy = water_in_kilograms * (final_temperature - initial_temperature) * 4184

print(f'The energy needed is {energy:.1f}')

