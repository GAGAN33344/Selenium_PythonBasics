# Classes are user defined blueprint or prototype, It should have methods, class variable,
# instance variables, constructor etc.
# Self Keyword is mandatory for calling variable names into method
# Instance and Class variables have whole different purpose
# Constructor name should be __init__
# New keyword is not required when we create object
class Calculator:
    num = 100 # Class Variables

    def __init__(self, a, b): # Parameterized Constructor
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically when object is created")

    def getdata(self):
        print("I am now executing as method in class")

    def summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num


obj = Calculator(2, 3) # Syntax to create objects in python
obj.getdata()
print(obj.num)
print(obj.summation())
