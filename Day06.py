class FlyingMixin:
    def fly(self):
        return f"{self.name} is flying to sky"

class SwimmingMixin:
    def swim(self):
        return f"{self.name} is swimming to sea"

class Pokemon:
    def __init__(self, name):
        self.name = name

class Charizard(Pokemon, FlyingMixin):
    pass

class Gyarados(Pokemon, SwimmingMixin):
    pass

p1 = Gyarados("Gyarados")
p2 = Charizard("Charizard")

print(p1.swim())
print(p2.fly())