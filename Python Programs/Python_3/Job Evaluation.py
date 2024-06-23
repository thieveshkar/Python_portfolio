#Author: Thieveshkar
#Task :Job Evaluation

def User_Age():
    while True:
        try:
            userage = int(input("Enter your age: "))
        except ValueError:
            print("Invalid input, please try again.")
        else:
            break
    return userage
    
def Education_Level():
    while True:
        try:
            education = input("Enter your Education Level (High School, Bachelor's, Master's, or PhD): ")
        except ValueError:
            print("Invalid input, please try again.")
        else:
            break
    return education
    
def Experience_Level():
    while True:
        try:
            experience = int(input("Enter your experience in years (integer): "))
        except ValueError:
            print("Invalid input, please try again.")
        else:
            break
    return experience
    
def Main_Program():
    userage = User_Age()
    education = Education_Level()
    experience = Experience_Level()
    
    if 25 <= userage <= 35 and (education == "Master's" or education == "PhD"):
        print("Congratulations! You are a strong candidate")
    elif experience == 3 and education == "Bachelor's":
        print("You are eligible")
    elif experience < 3 and education == "Bachelor's":
        print("Sorry, you do not meet the criteria for this position.")
    elif userage <= 25 and education == "PhD":
        print("You have an exceptional qualification")
    elif userage >= 36 and education == "Bachelor's":
        print("You have significant experience, but additional qualifications may be beneficial.")
    elif userage > 1 and experience > 1 and (education == "Bachelor's" or education == "High School" or education == "Master's" or education == "PhD"):
        print("You meet the basic criteria")
    elif userage > 20 and education is None and experience > 1:
        print("Sorry, you do not meet the criteria for this position.")
    else:
        print("Invalid criteria or input.")
    
Main_Program()





'''
Age=int(input("Enter you age: "))
Education=str(input("Enter your Education Level (High School, Bachelor's, Master's, or PhD): "))
Experence=int(input("Enter you Experence in the form of interger: "))
if Age<=35 and Age>=25 and Education=="Master's" or Education=="PhD":
    print("Congratulations! You are a strong candidate")
elif Experence==3 and Education=="Bachelor's":
    print("you are eligiable")
elif Experence<3 and Education=="Bachelor's":
    print("Sorry, you do not meet the criteria for this position.")
elif Age<=25 and Education=="PhD":
    print("you have a exceptional qualification")
elif Age>=36 and Education=="Bachelor's":
    print("You have significant experience, but additional qualifications may be beneficial.")
elif Age>1 and Experience>1 and Education=="Bachelor's" or Education=="High School" or Education=="Master's" or Education="PhD":
    print("Invalid age. Please enter a positive integer.")
elif Age>20 and Education==None and Experience>1:
    print("Sorry, you do not meet the criteria for this position.")
    
  '''  
