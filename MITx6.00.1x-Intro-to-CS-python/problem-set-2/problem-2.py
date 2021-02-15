"""
Write a program that calculates the minimum fixed monthly payment 
needed in order pay off a credit card balance within 12 months.
The monthly payment must be a multiple of $10 and is the same for all months.
"""

import math

balance = 3329
annualInterestRate = 0.2


def minPayment(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate / 12.0
    unpaidBalance = balance
    minimumPayment = 10
    unpaid = True
    while unpaid:
        months = 12
        while months > 0:
            unpaidBalance = unpaidBalance - minimumPayment
            unpaidBalance = unpaidBalance + \
                (monthlyInterestRate * unpaidBalance)
            months -= 1
        if unpaidBalance > 0:
            minimumPayment += 10
            unpaidBalance = balance
        else:
            unpaid = False
    return math.floor(minimumPayment)


print("Lowest Payment:", str(minPayment(balance, annualInterestRate)))
