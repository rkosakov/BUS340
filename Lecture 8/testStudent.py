from Student import Student

def main():
    s = Student('Maria', 5)
    print(s)

    s.setScore(1, 100)
    print(s)

    print(s.getHighScore())

    print(s.getAverage())

    print(s.getScore(1))

    print(s.getName())

main()
