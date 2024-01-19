class Pokemon:
    # constructor
    def __init__(self, name): # self-default, other-parameter
        self.name = name
        print(f"Create Pokemon {name}")

    def attack(self, target):
        print(f"{self.name} attacks {target.name}!")

pikachu = Pokemon("Pikachu")
squirtle = Pokemon("Squirtle")
charizard = Pokemon("Charizard")

pikachu.Lv = 10
pikachu.nemesis = squirtle
print(pikachu.Lv)
#print(pikachu.nemesis.Lv)  # Error
pikachu.nemesis.Lv = 9
print(squirtle.Lv)

print(charizard.name)

charizard.attack(pikachu)