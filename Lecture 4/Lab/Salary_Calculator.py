hours = eval(input('Enter hours worked: '))
salary = eval(input('Enrter salary per hour: '))

total_salary = 0
if hours > 40:
    total_salary = 40 * salary 
    overtime_hours = hours - 40
    overtime_salary = overtime_hours * (salary * (1 + 0.5))
    total_salary = total_salary + overtime_salary

else:
    total_salary = hours * salary

print(f'The Salary is: {total_salary:.2f}')
    
