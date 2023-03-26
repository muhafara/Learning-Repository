'''
Write a program to calculate the power of N
'''

def calPower(n):
    if n < 1:
        return "execution has ended"
    else:
        calPower(n)
        return n

print(calPower(5))