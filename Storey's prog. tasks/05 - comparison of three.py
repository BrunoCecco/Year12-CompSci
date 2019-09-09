#take 3 numbers and output the highest

a = int(input("enter a number"))
b = int(input("enter a number"))
c = int(input("enter a number"))
while a == b == c:  #if all numbers are the same, get new inputs
    a = int(input("enter a number"))
    b = int(input("enter a number"))
    c = int(input("enter a number"))
    
if a > b and a > c: # if a is largest, print A
    print("highest number was "a)
elif b > a and b > c: #if b is largest, print b
    print("highest number was "b)
else:
    print("highest number was "c) #otherwise c is largest, so print c

    
