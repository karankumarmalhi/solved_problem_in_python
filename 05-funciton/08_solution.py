def factorial(n):
    if n == 0:
        return 1
    else:
        # comment: 
        return n * factorial(n - 1)
    

print(factorial(2))