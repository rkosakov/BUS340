score = eval(input('Enter a score: '))

if score >= 90.0:
    grade = 'A'
else:
    if score >= 80.0:
        grade = 'B'
    else:
        if score >= 70.0:
            grade = 'C'
        else: 
            if score >= 60.0:
                grade = 'D'
            else:
                grade = 'F'
print('Your grade is', grade)


        