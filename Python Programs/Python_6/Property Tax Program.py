#Author: Thieveshkar
#Task :Property Taxes Program

def Userinput():
    while True:
        try:
            Property_Value=float(input("Enter the Value of the property: "))
        except ValueError:
            print("Invaild Input, please try again")
        else:
            break
    return Property_Value

def Assessment_Calculation(Property_Value):
    Assessment_Value=Property_Value*0.60
    return Assessment_Value

def Propery_Tax_Amount(Assessment_Value):
    Property_Tax=(Assessment_Value/100)*0.72
    return Property_Tax

def Tax_Calculator():
    while True:
        Property_Value=Userinput()
        Updated_Property_Value=round(Property_Value, 2)
        
        Assessment_Value=Assessment_Calculation(Property_Value)
        Updated_Assessment_Value=round(Assessment_Value, 2)
        
        Property_Tax=Propery_Tax_Amount(Assessment_Value)
        Updated_Property_Tax=round(Property_Tax, 2)
        
        
        print("for the property value of:", Updated_Property_Value, "you entered, the assessment value will be:", Updated_Assessment_Value, "and the property tax will be", Updated_Property_Tax)
        
        Option=input("Would you like to calculate again(yes/no)").strip().lower()
        if Option=="no":
            print("Thank you for using the program.")
            break
        elif Option=="yes":
            continue
        else:
            print("invaild input!, exiting the program....")
            break
        break    
        
Tax_Calculator()
        
    
            
