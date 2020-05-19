investmentValue = input("Please enter ammount of money you want to invest: ")
perAnnum = 10
yearlyValue = float(investmentValue)
numberOfYears = 0

while yearlyValue < 1000:
    numberOfYears += 1
    yearlyValue = yearlyValue +(yearlyValue * 10/100)

print("With an initial investment of ", investmentValue, " and ", perAnnum, "% interest rate")
print("Investment would take: ", numberOfYears, " to reach £1000")
    
