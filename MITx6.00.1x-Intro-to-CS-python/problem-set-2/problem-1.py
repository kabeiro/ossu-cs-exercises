"""
Write a program to calculate the credit card balance after one year
if a person only pays the minimum monthly payment 
required by the credit card company each month.
"""

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


def debtBalance(balance, annualInterestRate, monthlyPaymentRate):
    numOfMonths = 12
    unpaidBalance = balance
    while numOfMonths > 0:
        payment = unpaidBalance * monthlyPaymentRate
        unpaidBalance = unpaidBalance - payment
        unpaidBalance = unpaidBalance + \
            (annualInterestRate / 12.0 * unpaidBalance)
        numOfMonths -= 1
    return round(unpaidBalance, 2)


print('Remaining balance:', str(debtBalance(
    balance, annualInterestRate, monthlyPaymentRate)))
