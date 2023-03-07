'''
Write a code to work out how many 5p coins are needed to make £2.35
'''
#first we need to convert pound into pence
#one pound is equal to 100 pence 

given = 2.35
inPound = given * 100
penceToMakePound = inPound / 5

print(penceToMakePound)