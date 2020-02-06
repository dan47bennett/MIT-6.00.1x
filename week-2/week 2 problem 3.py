# calculate remaining balance after each month and output remainder after a year


balance = 999999
annualInterestRate = 0.18


def interestAfterMonths(balance, annualInterestRate, payment, numberOfMonths):
    for i in range(numberOfMonths):
        balanceAfterPayment = balance - payment
        interestDue = (annualInterestRate / float(numberOfMonths)) * balanceAfterPayment
        balance = balanceAfterPayment + interestDue
    finalBalance = round(balance, 2)
    return finalBalance


lowerBoundPayment = balance / 12.0
upperBoundPayment = (balance * (1 + (annualInterestRate / 12.0)) ** 12) / 12.0
payment = (lowerBoundPayment + upperBoundPayment) / 2.0

finalBalance = balance

while round(finalBalance, 2) != 0:
    finalBalance = interestAfterMonths(balance, annualInterestRate, payment, 12)
    if finalBalance <= 0:
        upperBoundPayment = payment
    else:
        lowerBoundPayment = payment
    payment = (lowerBoundPayment + upperBoundPayment) / 2.0


roundedPayment = round(payment, 2)
print("Lowest payment: " + str(roundedPayment))