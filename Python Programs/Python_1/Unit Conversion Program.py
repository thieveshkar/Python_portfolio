#Author: Thieveshkar
#Task :#Task 8: Unit Conversion Program:

def Unitconversion(UserInput):
    hours=UserInput*24
    minutes=UserInput*24*60
    seconds=UserInput*24*60*60
    return hours, minutes, seconds
  
usserInput=int(input("Enter the Days: "))

hr, mins, sec=Unitconversion(usserInput)
print("in hours:", hr )
print("in minutes:", mins )
print("in seconds:", sec)


