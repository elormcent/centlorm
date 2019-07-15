def factorial (z):
    if z == 1:
        return 1
    else:
        return z*factorial(z - 1)
        
print(factorial(4)) 