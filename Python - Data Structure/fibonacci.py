'''
using recersive, write a program to return a fibnocci number(n)
fibonacci series = 0 , 1, 1, 2, 3, 5, 8, 13.........n
fibnocci(5) return fibnocci number at position 5


fibnacci equation = fibonacci(n) = f(n-1) + f(n-2)

'''

def fibonacci(n):
    assert n >= 0 and int(n) == n, "The number should be a positive integer"
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci (n-2)
    

print(fibonacci(7))