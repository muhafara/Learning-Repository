#Write a Program which test the given number either it is even or odd

def even_odd_tester(number):
    if (number % 2 == 0):
        return "Even"
    else:
        return "Odd"


even_odd_tester(-123)