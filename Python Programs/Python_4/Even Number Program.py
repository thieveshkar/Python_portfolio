#Author: Thieveshkar
#Task :Even Number Program

Loopcount=0
EvenCount=0
Even=0
Average=0
for Number in range(1,8,1):
    Loopcount+=1
    Number=int(input('Enter the Number: '))
    if Number%2==0:
        EvenCount+=1
        Even+=Number
    elif Loopcount==7:
        break
    else:
        continue
Average=Even//EvenCount
print('the number of time you have entered a even number is:', EvenCount)
print('the total of all the even numbers you entered:', Even)
print('the average of all the even number you entered:', Average)  
    
    
    

    
