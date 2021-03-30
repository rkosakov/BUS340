def uniqueValues(list):
    uniqueNums = []
    for x in list:
        if x not in uniqueNums:
            uniqueNums.append(x)
    return uniqueNums

def counterOccur(uniqueNumbers, list):
    matchedList = []
    for x in uniqueNumbers:
        match = 0
        for y in list:
            if x == y:
                match = match+1
        matchedList.append(match)
    return matchedList

def reverse(List):
    revList = []
    for x in List:
        a = str(x)
        revList.append(a[::-1])
    return revList

def main():
    stop = True
    list = []
    while(stop):
        n = eval(input("Enter the integers between 10 and 9999 (0 to Exit): "))
        if n == 0:
            stop = False
        else:
            list.append(n)
    unVals = uniqueValues(list)
    com = counterOccur(unVals(list), list)
    for i in range(len(unVals)):
        if unVals[i] > 1:
            print(unVals[i], " occurs ", com[i], "times")
        else:
            print(unVals[i], " occurs ", com[i], "time")
    List = []

    for n in range(len(com)):
        if com[n] == 1:
            List.append(unVals[n])

    print("The unique numbers are: ", List)
    revList = reverse(List)
    for j in range(len(revList)):
        print(List[j], "  ->  ", revList[j])
    
main()