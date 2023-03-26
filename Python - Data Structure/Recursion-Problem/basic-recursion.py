'''
Basic recursive code
'''

def functionOne():
    functionTwo()
    print("I'm function one")

def functionTwo():
    functionThree()
    print("I'm function two")

def functionThree():
    functionFour()
    print("I'm function three")

def functionFour():
    print("I'm function four")

functionOne()