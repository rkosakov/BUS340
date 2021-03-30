class Student:
    def __str__(self):
        return "Student"
    
    def printStudent(self):
        print(self.__str__())

class GraduateStudent(Student):
    def __str__(self):
        return "Graduate student"

a = Student()
b = GraduateStudent()
a.printStudent()
b.printStudent()