import random

# My except
class Die(Exception):
    pass
class Finish(Exception):
    pass
class Clear(Exception):
    pass

# Pokemon abstract class
class Pokemon:
    def __init__(self, name, type, Lv, Hp, Deal):
        self.name = name
        self.type = type
        self.Lv = Lv
        self.Hp = Hp
        self.Deal = Deal

    def info(self):
        print(f"Name: {self.name}, Type: {self.type}, Lv: {self.Lv}, Hp: {self.Hp}, Deal: {self.Deal}\n")

    def Attack(self, target):
        print(f"{self.name} attack {target.name}")
        if self.type == 'Electric':
            print("Super-effective!!")
            target.Hp -= self.Deal * 2
        elif self.type == 'Grass':
            if target.type == 'Water':
                print("Super-effective!!")
                target.Hp -= self.Deal * 2
            elif target.type == 'Fire':
                print("Not very effective...")
                target.Hp -= int(self.Deal / 2)
            else:
                target.Hp -= self.Deal
        elif self.type == 'Fire':
            if target.type == 'Grass':
                print("Super-effective!!")
                target.Hp -= self.Deal * 2
            elif target.type == 'Water':
                print("Not very effective...")
                target.Hp -= int(self.Deal / 2)
            else:
                target.Hp -= self.Deal
        elif self.type == 'Water':
            if target.type == 'Fire':
                print("Super-effective!!")
                target.Hp -= self.Deal * 2
            elif target.type == 'Grass':
                print("Not very effective...")
                target.Hp -= int(self.Deal / 2)
            else:
                target.Hp -= self.Deal


class Pikachu(Pokemon):
    def __init__(self):
        super().__init__('Pikachu', 'Electric', 30, 50, 23)

class Turtwig(Pokemon):
    def __init__(self):
        super().__init__('Turtwig', 'Grass', 10, 20, 7)

class Chimchar(Pokemon):
    def __init__(self):
        super().__init__('Chimchar', 'Fire', 10, 20, 7)

class Piplup(Pokemon):
    def __init__(self):
        super().__init__('Piplup', 'Water', 10, 20, 7)

# main
Wild = ['Bidoof', 'Eevee', 'Magikarp', 'Gyarados', 'Squirtle', 'Ponyta', 'Charmeleon', 'Roselia', 'Torterra']
w_Type = ['Normal', 'Normal', 'Water', 'Water', 'Water', 'Fire', 'Fire', 'Grass', 'Grass']
p1 = Pikachu(); p2 = Turtwig(); p3 = Chimchar(); p4 = Piplup();
Starting = [p1, p2, p3, p4]

StartNum = int(input("Choose your starting Pokemon\n1) Turtwig   2) Chimchar   3) Piplup : "))
MyPokemon = Starting[StartNum]
print("Your starting Pokemon is", end= ' ')
MyPokemon.info()

while True:
    try:
        if MyPokemon.Lv >= 100:
            raise Clear
        WildNum = random.randint(0, 8)
        WildLv = random.randint(1, 100)
        WP = Pokemon(Wild[WildNum], w_Type[WildNum], WildLv, int(WildLv * 1.2), int(WildLv * 0.5))
        print(f"Wild Pokemon {WP.name}(Lv.{WP.Lv}) is appeared!")
        while True:
            MySelect = int(input(f"What will {MyPokemon.name} do?\n1) Fight   2) Run   3) Info   4) Quit : "))
            if MySelect == 1:
                MyPokemon.Attack(WP)
                WP.Attack(MyPokemon)
                print()
                if MyPokemon.Hp <= 0:
                    raise Die()
                if WP.Hp <= 0:
                    reward = int(WP.Lv * 0.2)
                    MyPokemon.Lv += reward
                    MyPokemon.Hp += reward * 4
                    MyPokemon.Deal += int(reward * 1.5)
                    print(f"{WP.name} is dead\n{MyPokemon.name} get {reward}exp\n")
                    break
            elif MySelect == 2:
                if WP.Lv - MyPokemon.Lv >= 5:
                    print("You got away safely!\n")
                    break
                else:
                    print("You couldn't get away!\n")
            elif MySelect == 3:
                MyPokemon.info()
                WP.info()
            else:
                raise Finish
    except Die:
        s1 = "Your Pokemon is dead"
        s2 = "Game Over"
        print(s1.center(20))
        print(s2.center(20))
        break
    except Finish:
        s1 = "Power is off"
        s2 = "See you next time"
        print(s1.center(20))
        print(s2.center(20))
        break
    except Clear:
        s1 = "!!! Congraturation !!!"
        s2 = "You become a Pokémon Master."
        print(s1.center(30))
        print(s2.center(30))
        break