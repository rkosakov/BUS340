from Loan import Loan

def main():
    annualInterestRate = eval(input ("Enter yearly interest rate, for example, 7.25: "))
    numberOfYears = eval(input("Enter number of years as an integer: "))
    loanAmount = eval(input("Enter loan amount, for example, 120000.95: "))
    borrower = input("Enter a borrower's name: ")

    loan = Loan(annualInterestRate, numberOfYears, loanAmount, borrower)
    loan.__str__()

main()

