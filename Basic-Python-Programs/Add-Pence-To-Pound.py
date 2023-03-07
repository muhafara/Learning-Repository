'''
Write a code to add 61p to £1.35
'''

givenPence = 61
givenPound = 1.35

totalPound = (((givenPound * 100) + givenPence)) /100

print(f"{givenPence}p added to £{givenPound} is £{totalPound}")