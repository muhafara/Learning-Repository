'''
Write a code to calculate how much in metre be added to 850m to make 1.5km.
'''

#To begin with we need to convert km metre to metre by mutiplying by 1000
givenMetre = 850
givenKm = 1.5

# using int() to convert float value into integer

metreRequired = int((givenKm * 1000) - givenMetre) # converted into metre which is 1500 metre

print(f"TO make {givenKm} km we need to add {metreRequired}m in {givenMetre}m")
