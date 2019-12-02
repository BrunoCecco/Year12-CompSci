Num1 = int(input("Enter a times table"))
Num2 = int(input("Enter a start number"))
Num3= int(input("Enter the end number"))
table = 0
def multiples(Num1, Num2, Num3):
    for i in range(Num2, Num3+1):    
        table = Num1 * Num2
        print(Num1, ' x ', Num2, ' = ', table)
        Num2 += 1
	
multiples(Num1, Num2, Num3)

