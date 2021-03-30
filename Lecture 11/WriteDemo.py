def main():

    openfile = open("Presidents.txt", "w")

    openfile.write("Bill Clinton\n")
    openfile.write("George Bush\n")
    openfile.write("Barak Obama\n")

    openfile.close()
    openfile = open("Presidents.txt", "a")
    openfile.write("\nPython is interpreted\n")
    openfile.close()

    openfile = open("Presidents.txt", "r")

    print("Using read() method: ")
    print(openfile.read())

    print(openfile.tell())
    openfile.seek(0, 0)
    print(openfile.read())
    openfile.close()


main()
