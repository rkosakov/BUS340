numberStudents = eval(input('Enter the number of students: '))

highestScore = 0
secondHighestScore = 0
middleScore = 0

highestName = ''
middleName = ''
secondName = ''

for i in range(1, numberStudents + 1):
    student = input('Enter a student name: ')
    score = eval(input('Enter a score for the student: '))

    if score > highestScore:
        middleScore = highestScore
        highestScore = score
        secondHighestScore = middleScore

        middleName = highestName
        highestName = student
        secondName = middleName

print(f'Student {highestName} has the highest score of {highestScore}')
print(f'Student {secondHighestScore} has the second highest score of {secondHighestScore}')

       
    
    


