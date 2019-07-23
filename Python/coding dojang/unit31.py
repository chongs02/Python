def fib(n, a1=0, a2 = 1):
    result = a1
    if n == 0:
        return result
    else :
        return fib(n-1, a2, a1+a2)
    
    
print(fib(10))    
