class Pokemon:
    def __init__(self, input_name):
        self.__name = input_name # name mangling __(variable name)
    @property # getter
    def name(self): # getter name
        return self.__name
    @name.setter # (getter name).setter
    def name(self, new_name): # should be same as getter name
        self.__name = new_name

p1 = Pokemon("Gyarados")
print(p1.name)
p1.name = "Magikarp"
print(p1.name)
p1.__name = "Gyarados" # Nothing change
print(p1.name)