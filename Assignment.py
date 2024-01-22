import random
from Pokemon import *
# My except
class Die(Exception):
    pass
class Finish(Exception):
    pass
class Clear(Exception):
    pass

# Evolution mixin class
class Evolution:
    def evol(self, n):
        print(f"Congratulations!Your {self.name}\nevolved into {n}")
        self.name = n
        self.hp += 5
        self.deal += 2

# Starting pokemon classes
class Pikachu(Pokemon):
    def __init__(self):
        super().__init__('Pikachu', 'Electric', 30, 71, 25)
class Turtwig(Pokemon, Evolution):
    def __init__(self):
        super().__init__('Turtwig', 'Grass', 10, 27, 9)
class Chimchar(Pokemon, Evolution):
    def __init__(self):
        super().__init__('Chimchar', 'Fire', 10, 27, 9)
class Piplup(Pokemon, Evolution):
    def __init__(self):
        super().__init__('Piplup', 'Water', 10, 27, 9)

# My Func
def isAdvanced(a, b) -> bool:
    if a.type == 'Electric' and (b.type != 'Psychic' or b.type != 'Dragon'):
        return True
    if a.type == 'Grass' and b.type == 'Water':
        return True
    if a.type == 'Water' and b.type == 'Fire':
        return True
    if a.type == 'Fire' and b.type == 'Grass':
        return True
    return False
def isEvolution(a, b) -> bool:
    if a.lv >= b:
        return True
    return False

# main
Wild = ['Bidoof', 'Eevee', 'Magikarp', 'Squirtle', 'Ponyta', 'Roselia', 'Charmeleon', 'Gyarados', 'Torterra', 'Mewtwo', 'Dialga', 'Palkia']
w_Type = ['Normal', 'Normal', 'Water', 'Water', 'Fire', 'Grass', 'Fire', 'Water', 'Grass', 'Psychic', 'Dragon', 'Dragon']
p1 = Pikachu(); p2 = Turtwig(); p3 = Chimchar(); p4 = Piplup();
Starting = [p1, p2, p3, p4]

# set My_Pokemon
StartNum = int(input("Choose your starting Pokemon\n1) Turtwig   2) Chimchar   3) Piplup : "))
MyPokemon = Starting[StartNum]
print("Your starting Pokemon is", end= ' ')
MyPokemon.info()
print()

while True:
    # if flag is True you can run from wild Pokemon
    if StartNum == 0:
        flag = True
    else:
        flag = False

    # Evolution
    if isEvolution(MyPokemon, 25):
        if MyPokemon.name == 'Turtwig':
            MyPokemon.evol('Grotle')
            print()
        elif MyPokemon.name == 'Chimchar':
            MyPokemon.evol('Monferno')
            print()
        elif MyPokemon.name == 'Piplup':
            MyPokemon.evol('Prinplup')
            print()
    if isEvolution(MyPokemon, 55):
        if MyPokemon.name == 'Grotle':
            MyPokemon.evol('Torterra')
            print()
        elif MyPokemon.name == 'Monferno':
            MyPokemon.evol('Infernape')
            print()
        elif MyPokemon.name == 'Prinplup':
            MyPokemon.evol('Empoleon')
            print()

    # In Game
    try:
        if MyPokemon.lv >= 100:
            raise Clear

        # set Wild_Pokemon
        if MyPokemon.lv <= 20:
            WildNum = random.randint(0, 4)
        elif MyPokemon.lv <= 50:
            WildNum = random.randint(5, 8)
        elif MyPokemon.lv <= 80:
            WildNum = random.randint(7, 8)
        else:
            WildNum = random.randint(7, 11)

        if MyPokemon.lv <= 30:
            WildLv = random.randint(MyPokemon.lv - 5, MyPokemon.lv + 3)
        elif MyPokemon.lv <= 70:
            WildLv = random.randint(MyPokemon.lv - 3, MyPokemon.lv + 7)
        elif MyPokemon.lv <= 93:
            WildLv = random.randint(MyPokemon.lv, MyPokemon.lv + 7)
        else:
            WildLv = 100

        WildPokemon = Pokemon(Wild[WildNum], w_Type[WildNum], WildLv, int(WildLv * 1.5) + 3, int(WildLv * 0.7))
        if WildNum == 9 or WildNum == 10 or WildNum == 11 and WildLv <= 90:
            WildLv += 5; WildPokemon.hp += 8; WildPokemon.deal += 10;
        print(f"Wild Pokemon {WildPokemon.name}(Lv.{WildPokemon.lv}) is appeared!")

        # User select
        while True:
            MySelect = int(input(f"What will {MyPokemon.name} do?\n1) Fight   2) Run   3) Info   4) Quit : "))
            if MySelect == 1:
                MyPokemon.Attack(WildPokemon)
                if WildPokemon.hp <= 0:
                    reward = int(WildPokemon.lv * 0.05) + 1
                    MyPokemon.lv += reward
                    MyPokemon.hp += int(reward * 18.5) - 13
                    MyPokemon.deal += int(reward * 0.9) + 0.5
                    print(f"\n{WildPokemon.name} is dead\n{MyPokemon.name} get {reward}exp\n")
                    break
                WildPokemon.Attack(MyPokemon)
                print()
                if MyPokemon.hp <= 0:
                    raise Die()

            elif MySelect == 2:
                if WildPokemon.lv - MyPokemon.lv <= 5 or flag:
                    print("You got away safely!\n")
                    break
                else:
                    flag = True
                    print("You couldn't get away!")
                    WildPokemon.Attack(MyPokemon)
                    print()
                    if MyPokemon.hp <= 0:
                        raise Die()
            elif MySelect == 3:
                print("Your Pokemon:")
                MyPokemon.info()
                print("Wild Pokemon:")
                WildPokemon.info()
                if isAdvanced(MyPokemon, WildPokemon) and WildNum != 9 and WildNum != 10 and WildNum != 11:
                    print("Your Pokemon has advantaged!")

                if WildPokemon.lv - MyPokemon.lv <= 5 or flag:
                    print(f"You can run from {WildPokemon.name}\n")
                else:
                    print(f"You can't run from {WildPokemon.name}\n")
            elif MySelect == 4:
                raise Finish
            else:
                print("Please select a valid menu\n")

    # Exception handling
    except Die:
        s1 = "Your Pokemon is dead..."
        s2 = "Game Over"
        print(s1.center(20))
        print(s2.center(20))
        break
    except Finish:
        s1 = "Power is off"
        s2 = "See you next time~"
        print(s1.center(20))
        print(s2.center(20))
        break
    except Clear:
        s1 = "!!! Congraturation !!!"
        s2 = "You become a Pokémon Master."
        print(s1.center(30))
        print(s2.center(30))
        break