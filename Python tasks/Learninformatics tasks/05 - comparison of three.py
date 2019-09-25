#take 3 numbers and output the highest

a = int(input("enter a number"))
b = int(input("enter a number"))
c = int(input("enter a number"))
while a == b == c:  #if all numbers are the same, get new inputs
    a = int(input("enter a number"))
    b = int(input("enter a number"))
    c = int(input("enter a number"))
    
if a > b and b > c and a > c: # if a is largest, print A
    print(a, b, c)
elif a > b and c > b and a > c:
    print(a, c, b)
elif b > a and b > c and c > a:
    print(b, c, a)
elif b > a and b > c and a > c: #if b is largest, print b
    print(b, a, c)
elif c > b and c > a and b > a:
    print(c, b, a)
else:
    print(c, a, b) #otherwise c is largest, so print c

    
