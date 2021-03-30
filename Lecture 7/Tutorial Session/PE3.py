def getInput():
    numbers = {}
    flag = True

    while flag == True:
        number = eval(input('Enter the integers between 10 and 9999 (0 to Exit): '))

        if number == 0:
            flag = False
            continue
       
        if number not in  numbers:
            numbers[number] = 1
        else:
            numbers[number] += 1
        
        
    return numbers

def printDict(numbers):
    for key in numbers:
        print(f'{key} occurs {str(numbers[key])} times')

def uniqueNums(numbers):
    print('The unique numbers are: ', end = ' ')
    for key in numbers:
        if numbers[key] == 1:
            
            print(key, end = ' , ')
        
def reverse(numbers):
    reversed = []
    for key in numbers:
        if numbers[key] == 1:
            num = str(key)
            revNum = num[::-1]
            reversed.append(revNum)
    return reversed

def PrintReversed(numbers, reversed):
        
    print('The unique numbers in reverse order:')
    for num in numbers:

        if numbers[num] == 1:
            print(f'{numbers[num]} -> {reversed[num]}')
    



def main():
    numbers = getInput()
    printDict(numbers)
    unique = uniqueNums(numbers)
    print()
    reversedNums = reverse(numbers)
    PrintReversed(numbers, reversedNums)
    

main()
