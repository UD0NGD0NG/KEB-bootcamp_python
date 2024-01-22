class Class:
    name = 'First' # Basic class attribute
    cnt = 0
    def __init__(self): # Constructor
        Class.cnt += 1
    @classmethod # affects class and all objects
    def getCount(cls): # parameter must be cls
        return cls.cnt
    def __str__(self): # Magic method (operator overloading)
        return (f"My name is {self.name}")

class_one = Class()
print(f"class1's name: {class_one.name}")
class_one.name = 'Change'
print(f"now class1's name: {class_one.name}") # change object's attribute
Class.name = "Second" # change class attribute
class_two = Class()
print(f"class1's name: {class_one.name}")
print(f"class2's name: {class_two.name}") # == Changed class attribute

print(Class.cnt)
print(class_one.cnt)

print(class_one)
print(class_two)