# calculate remaining balance after each month and output remainder after a year


balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


def interestAfterMonths(balance, annualInterestRate, monthlyPaymentRate, numberOfMonths):
    for i in range(numberOfMonths):
        thisMonthsPayment = monthlyPaymentRate * balance
        balanceAfterPayment = balance - thisMonthsPayment
        interestDue = (annualInterestRate / float(numberOfMonths)) * balanceAfterPayment
        balance = balanceAfterPayment + interestDue
    finalBalance = round(balance, 2)
    return finalBalance

finalBalance = interestAfterMonths(balance, annualInterestRate, monthlyPaymentRate, 12)
print("Remaining balance: " + str(finalBalance))