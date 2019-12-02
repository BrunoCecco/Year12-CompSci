Spaces =[["", "", "", "", "", ""],
         ["", "", "", "", "", ""],
         ["", "", "", "", "", ""],
         ["", "", "", "", "", ""],
         ["", "", "", "", "", ""],
         ["", "", "", "", "", ""],
         ["", "", "", "", "", ""],
         ["", "", "", "", "", ""],
         ["", "", "", "", "", ""],
         ["", "", "", "", "", ""]]
def emptyPark():
    print("Parking size is : %d by %d" % (len(Spaces), len(Spaces[0])))
    for i in range(len(Spaces)):
        for j in range(len(Spaces[0])):
            Spaces[i][j] = "empty"    
def parkCar(row, column, reg_num):
    if row < 1 or row > 10 or column < 1 or column > 6:
        return "Invalid input"
    if Spaces[row-1][column-1] == "empty":
        Spaces[row-1][column-1] = reg_num
        return "Ok"
    return "Parking space taken"
def printGrid():
    for i in range(len(Spaces)):
        print("Row: %d " % (i+1), end='')
        for j in range(len(Spaces[0])):
            print("%s\t" % Spaces[i][j], end='')
        print()
# main program
emptyPark()
while True:    
    Reg_num = input("Enter registration number: ")
    while True:
        Row = int(input("Enter row: "))
        Column = int(input("Enter column: "))
        result = parkCar(Row, Column, Reg_num)
        if result != "Ok":
            print(result)
            continue
        printGrid()
        break
