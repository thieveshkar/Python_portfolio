#Author: Thieveshkar
#Task :Temperature Analysis

Temperature = []

def Userinput():
    while True:
        try:
            userinput = int(input("Enter the number of days: "))
            if userinput <= 0:
                print("Invalid input. Please enter a positive integer.")
                continue
        except ValueError:
            print("Invalid input, please try again.")
        else:
            return userinput

def Loop_Program(userinput):
    for day in range(userinput):
        while True:
            try:
                Daily_Temperature = float(input(f"Enter the temperature for day {day + 1}: "))
                Temperature.append(Daily_Temperature)
                break
            except ValueError:
                print("Invalid input. Please enter a valid temperature.")
    
    Max_Temperature = max(Temperature)
    Min_Temperature = min(Temperature)
    total = sum(Temperature)
    Average_Temperature = round(total / userinput, 2)
    
    return Max_Temperature, Min_Temperature, Average_Temperature

def Main_Program():
    userinput = Userinput()
    Max_Temperature, Min_Temperature, Average_Temperature = Loop_Program(userinput)
    
    print(f"Highest temperature recorded: {Max_Temperature}")
    print(f"Lowest temperature recorded: {Min_Temperature}")
    print(f"Average temperature: {Average_Temperature:.2f}")
    
    print("Days with temperatures above the average:")
    for i, temp in enumerate(Temperature):
        if temp > Average_Temperature:
            print(f"Day {i + 1}: {temp}")

Main_Program()
