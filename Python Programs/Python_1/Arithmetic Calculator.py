#Author: Thieveshkar
#Task :Basic Arithmetic Calculator

Number_1=float(input("Enter the First Number: "))
Number_2=float(input("Enter the Second Number: "))
Userinput=input("Please type Add to add, Sub to Substract, Multiply to Multiply and Divide to divide: ")
if Userinput=="Add":
    Output=Number_1+Number_2
elif Userinput=="Sub":
    Output=Number_1-Number_2
elif Userinput=="Multiply":
    Output=Number_1*Number_2
elif Userinput=="Divide":
    Output=Number_1/Number_2
else:
    print("Invaild Input")
float(Output)   
print(Output)