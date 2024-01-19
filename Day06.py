name = "Name"

def Unchangeable():
    name = "UC_Name"
    print(name, id(name))

def Changeable():
    global name
    name = "C_Name"
    print(name, id(name))

print(name, id(name))
Unchangeable()
print(name, id(name))
Changeable()
print(name, id(name))