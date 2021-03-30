def PentagonialNumber(n):
    return (3*n*n - n)/2

def displayPentNumbers():
    for num in range(1, 11):
        print(PentagonialNumber(num), ' ', end = '')

def main():
    displayPentNumbers()

main()