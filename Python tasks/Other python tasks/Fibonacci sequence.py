def fib(n):
    if n <=1:
        print(n)
    else:
        return fib(n-1) + fib(n-2)
fibonacci = fib(5)
    
print(fibonacci)
