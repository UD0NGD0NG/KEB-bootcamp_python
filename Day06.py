class Animal:
    def say(self):
        print("I speak!")

class Horse(Animal):
    def say(self):
        print("Horse speak!")

class Donkey(Animal):
    def say(self):
        print("Donkey speak!")

class Mule(Donkey, Horse):
     def say(self):
         print("Mule speak!")

class Hinny(Horse, Donkey): # if Horse class has say call Horse's say else if Donkey class has say call Donkey's say else call Animal's say
    pass

mule = Mule()
hinny = Hinny()

mule.say()
hinny.say()