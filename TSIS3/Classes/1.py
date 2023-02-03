'''1. Define a class which has at least two methods: getString: 
to get a string from console input printString: to print the string in upper case.
'''

class Str():
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input()
    
    def printString(self):
        print(self.string.upper())


s = Str()
s.getString()
s.printString()
