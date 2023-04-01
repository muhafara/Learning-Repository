'''
Using recersive write a program to calculate the sumof a digit
For example
123 = 1 + 2 + 3 = 6
s(n) = n/10 +f(n % 10) 
'''

def sumDigits(n):
    if n in [0]:
        return 0
    else:
        return int(n % 10) + sumDigits(n // 10)


print(sumDigits(123))