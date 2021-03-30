def LowerCounter(word):
    lowerCount = 0
    for i in word:
        if i.islower():
            lowerCount += 1
    
    return lowerCount

def UpperCounter(word):
    upperCount = 0
    for i in word:
        if i.isupper():
            upperCount += 1

    return upperCount

def main(): 

    lower = LowerCounter('Some String')
    upper = UpperCounter('Some String')

    print(lower)
    print(upper)

main()

