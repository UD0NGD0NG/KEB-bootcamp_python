class Pokemon:
    def __init__(self, name):
        self.name = name

    def attack(self, target):
        print(f"{self.name}이(가) {target.name}을(를) 공격!")

class Pikachu(Pokemon): # inherit(is-a)
    def __init__(self, name, type):
        super().__init__(name) # Delegation
        self.type = type

    def attack(self, target):
        print(f"{self.name}이(가) {target.name}을(를) {self.type} 공격!")

    def attack_info(self):
        print(f"{self.type} 계열의 공격을 합니다.")

class Squirtle(Pokemon):
    pass

p1 = Pikachu("피카츄", "전기")
p2 = Squirtle("꼬부기")
p3 = Pokemon("미싱노")

print(p1.name)
p1.attack(p2)
p2.attack(p1)

p1.attack_info()
#p3.attack_info()  # Error, attack_info is personality