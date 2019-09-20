Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

Max = 0
Min = 100
for i in range(1, 6):
    Letter = str(input("Enter a lowercase letter"))
    if Alphabet.index(Letter) < Min:
        Min = Alphabet.index(Letter)
    elif Alphabet.index(Letter) > Max:
        Max = Alphabet.index(Letter)
	#Endif
#Next
print("Largest letter was: " + Alphabet[Max])
print("Smallest number was: " + Alphabet[Min])
