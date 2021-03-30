from random import randint

def main():

    outfile = open("Numbers.txt", "w")

    for i in range(10):
        outfile.write(str(randint(0, 9)) + " ")
    outfile.close()

    infile = open("Numbers.txt", "r")
    s = infile.read()
    numbers = [eval(x) for x in s.split()]

    for num in numbers:
        print(num, end = " ")
    infile.close()

main()

