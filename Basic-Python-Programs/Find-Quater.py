'''
Write a code to work out three quarters of £4.32
'''

givenValue = 4.32
requiredQuaters = 3

#Convert given value £4.32 into pence 1 pound = 100 pence

quaterRequired = (((givenValue * 100) / 4) * requiredQuaters) / 100

print(f"{requiredQuaters} quaters of £{givenValue} is £{quaterRequired}")

