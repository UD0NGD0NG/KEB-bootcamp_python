class Behavior:
    def __init__(self, method):
        self.method = method
class Skill:
    def __init__(self, sk):
        self.sk = sk
    def use(self):
        return self.sk
class Pokemon:
    def __init__(self, name, tmp):
        self.name = name
        self.tmp = tmp
        self.skill = Skill('Tackle') # Composition
    def Fly(self):
        if self.tmp.method == 'Wings':
            print(f"{self.name} is flying to sky by {self.tmp.method}")
        else:
            print(f"{self.name} can't fly")
    def Swim(self):
        if self.tmp.method == 'Tails':
            print(f"{self.name} is swimming to sea by {self.tmp.method}")
        else:
            print(f"{self.name} can't swim")
    def Attack(self):
        print(f"{self.name} is attacked by {self.skill.use()}")
class Charizard(Pokemon):
    pass
class Gyarados(Pokemon):
    pass

# Aggregation
wings = Behavior('Wings')
tails = Behavior('Tails')

p1 = Gyarados("Gyarados", tails)
p2 = Charizard("Charizard", wings)

p1.Fly()
p1.Swim()
p2.Fly()
p2.Swim()


# Composition
p1.Attack()