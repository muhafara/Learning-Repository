'''
Using recursive write a program to print a number upto n
Define base condition which is n >=1
'''

def printNumber(n):
    if n < 1:
        print("Recursive hits its based conditon")
    else:
        printNumber(n-1)
        print(n)

printNumber(5)