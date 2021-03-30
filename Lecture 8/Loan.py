class Loan:
    def __init__(self, annualInterestRate = 2.5, \
        numberOfYears = 1, loanAmount = 1000, borrower = ""):

        self.__annualInterestRate = annualInterestRate
        self.__numberOfYears = numberOfYears
        self.__loanAmount = loanAmount
        self.__borrower = borrower

    def getAnualInterestRate(self):
        return self.__annualInterestRate

    def getNumberOfYears(self):
        return self.__annualInterestRate
    
    def getLoanAmount(self):
        return self.__loanAmount
    
    def getBorrower(self):
        return self.__borrower
    
    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate
    
    def setNumberOfYears(self, numberOfYears):
        self.__numberOfYears = numberOfYears
    
    def setLoanAmount(self, loanAmount):
        self.__loanAmount = loanAmount
    
    def setBorrower(self, borrower):
        self.__borrower = borrower
    
    def getMonthlyPayment(self):
        montlyInterestRate = self.__annualInterestRate / 1200
        montlyPayment = self.__loanAmount * montlyInterestRate / (1-(1 / (1 + montlyInterestRate)**(self.__numberOfYears * 12)))
        return montlyPayment
    
    def getTotalPayment(self):
        totalPayment = self.getMonthlyPayment() * self.__numberOfYears * 12
        return totalPayment

    def __str__(self):
        print("The loan is for", self.getBorrower())
        print("The monthly payment is", format(self.getMonthlyPayment(), ".2f"))
        print("The total payment is", format(self.getTotalPayment(), ".2f"))
    
        