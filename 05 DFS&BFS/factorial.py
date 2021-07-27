def factorial(n):
    result=1
    for i in range(1,n+1):
        result *= i
    return result

def factoial_recursive(n):
    if n <= 1:
        return 1
    return n*factoial_recursive(n-1)

print(factorial(5))
print(factoial_recursive(5))

    
