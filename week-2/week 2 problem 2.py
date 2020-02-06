# calculate remaining balance after each month and output remainder after a year


balance = 3926
annualInterestRate = 0.2


def interestAfterMonths(balance, annualInterestRate, payment, numberOfMonths):
    for i in range(numberOfMonths):
        balanceAfterPayment = balance - payment
        interestDue = (annualInterestRate / float(numberOfMonths)) * balanceAfterPayment
        balance = balanceAfterPayment + interestDue
    finalBalance = round(balance, 2)
    return finalBalance


payment = 0
finalBalance = balance

while(finalBalance >= 0):
    payment += 10
    finalBalance = interestAfterMonths(balance, annualInterestRate, payment, 12)


print("Lowest payment: " + str(payment))