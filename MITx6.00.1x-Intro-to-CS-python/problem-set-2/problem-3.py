"""
Write a program that calculates the minimum fixed monthly payment 
needed in order pay off a credit card balance within 12 months.
Using Bisection Search
"""

balance = 999999
annualInterestRate = 0.18


def minPayment(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate / 12.0
    monthlyPaymentLowerBound = balance / 12
    monthlyPaymentUpperBound = balance * \
        ((1 + monthlyInterestRate) ** 12) / 12.0
    minimumPayment = (monthlyPaymentUpperBound +
                      monthlyPaymentLowerBound) / 2.0
    while monthlyPaymentLowerBound < (monthlyPaymentUpperBound - 0.01):
        months = 12
        unpaidBalance = balance
        minimumPayment = (monthlyPaymentUpperBound +
                          monthlyPaymentLowerBound) / 2.0
        while months > 0:
            unpaidBalance = unpaidBalance - minimumPayment
            unpaidBalance = unpaidBalance + \
                (monthlyInterestRate * unpaidBalance)
            months -= 1
        if unpaidBalance <= 0:
            monthlyPaymentUpperBound = minimumPayment
        else:
            monthlyPaymentLowerBound = minimumPayment
    return round(minimumPayment, 2)


print("Lowest Payment:", str(minPayment(balance, annualInterestRate)))
