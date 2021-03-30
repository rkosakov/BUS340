def IsLeapYear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
             return True
    else:
        return False
        
def main():
    done = True
    while done:
        year = eval(input("Enter a year (0 to exit): "))
        if year == 0: 
            done = False
            continue

        if year < 1900 or year > 2020:
            print("The year must be in the range [1900, 2020].")
        else:
            if(IsLeapYear(year)):
                print(year, "is a Leap Year")
            else:
                print(year, "is Not a Leap Year")

main()


    