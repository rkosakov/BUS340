from BMI import BMI

def main():
    bmi1 = BMI("John Doe", 18, 145, 70)
    

    bmi2 = BMI("Peter King", 50, 215, 70)
    
    print(bmi1.__str__())
    print(bmi2.__str__())

main() 