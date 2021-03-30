from math import pow
weight = eval(input('Enter weight in pounds: '))
height = eval(input('Enter height in inches: '))

kilograms = 0.45359237 * weight
centimeters = 0.0254 * height
bmi = kilograms / (pow(centimeters, 2))
print(f'BMI is {bmi:.2f}')

if bmi < 18.5:
    print('Underweight')
elif bmi >= 18.5 and bmi <= 24.9:
    print('Normal')
elif bmi >= 25.0 and bmi <= 29.9:
    print('Overweight')
elif bmi >= 30.0:
    print('Obese')
else:
    print('Error')