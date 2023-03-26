'''
Using recersive method, write a program to print factorial of n number.
'''

#factorial equation : n * (n-1) * (n-2) * (n-3)

def factorial(n):
    assert n >= 0 and int(n)==n, "The number must be greater than 0 and positive integer"
    #base condition
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)
    

print(factorial(5))