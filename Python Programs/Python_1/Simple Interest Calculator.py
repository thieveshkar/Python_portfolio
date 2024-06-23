#Author: Thieveshkar
#Task :#Simple Interest Calculator


def Interest_Calculator(amount, period, interestrate):
    calculation=amount*(1+period*interestrate)
    return calculation
    
Principal_Amount=float(input("Please enter the Principal Amount: "))
Period=int(input("Enter the time period in years: "))
Interest_Rate=float(input("Enter the Interest Rate: "))



Caluculated_Value=Interest_Calculator(Principal_Amount, Period, Interest_Rate )
print(Caluculated_Value)