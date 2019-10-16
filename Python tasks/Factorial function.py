"""
def fact(m):
    
    factorial = 1
    for count in range(1, m+1):
        factorial = factorial * count
    #next
    return factorial
#end function

n = int(input("Enter a number"))
ans = fact(n)
print(n, "Factorial = ", ans)
"""
def fact(m):
    if m == 0:
        factorial = 1
    else:
        factorial = m * fact(m-1)
    #endif
    return factorial
#end function

n = int(input("Enter a number"))
ans = fact(n)
print(n, "Factorial = ", ans)
