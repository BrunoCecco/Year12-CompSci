Names = [" ", " ", " "," ", " ", " ", " ", " ", " ", " " ]
Number = int()
def displayMenu():
    global Number
    print("1. Add name")
    print("2. Display list")
    print("3. Quit")
    Number = int(input("Enter your choice: "))
    while Number < 1 or Number > 3:
        Number = int(input("Invalid choice - please re-enter: "))
def choice1():
    Name = str(input("Enter the name to be added to the list: "))
    List_index = int(input("Enter the position ni the list to insert the name (1-10): "))
    Names[List_index] = Name
def choice2():
    for i in range(len(Names)):
        print(Names[i])
Choice = displayMenu()
while Number != 3:    
    if Number == 1:
        choice1()
        displayMenu()
    elif Number == 2:
        choice2()
        displayMenu()
print("Program terminating")
