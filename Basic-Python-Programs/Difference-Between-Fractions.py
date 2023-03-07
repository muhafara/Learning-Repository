'''
Write a code to work out the difference between £ 1/5 and £ 1/4 . Your answer must be positive
'''

onePound = 100

differenceBetween = int((onePound / 4) - (onePound / 5))

'''
We can also use abs() function to convert negative value to positive
'''
# differenceBetween = int(abs((onePound / 5) - (onePound / 4)))

print(f"Diffrence between £1/5 and $ 1/4 is {differenceBetween}")
