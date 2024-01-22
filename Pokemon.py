class Pokemon:
    def __init__(self, name, type, lv, hp, deal):
        self.__Name = name
        self.__Type = type
        self.__Lv = lv
        self.__Hp = hp
        self.__Deal = deal

    @property
    def name(self):
        return self.__Name
    @name.setter
    def name(self, new_name):
        self.__Name = new_name
    @property
    def type(self):
        return self.__Type
    @type.setter
    def type(self, new_type):
        self.__Type = new_type
    @property
    def lv(self):
        return self.__Lv
    @lv.setter
    def lv(self, new_lv):
        self.__Lv = new_lv
    @property
    def hp(self):
        return self.__Hp
    @hp.setter
    def hp(self, new_hp):
        self.__Hp = new_hp
    @property
    def deal(self):
        return self.__Deal
    @deal.setter
    def deal(self, new_deal):
        self.__Deal = new_deal
    def info(self):
        print(f"Name: {self.__Name}, Type: {self.__Type}, Lv: {self.__Lv}, Hp: {self.__Hp}, Deal: {self.__Deal}")
    def Attack(self, target):
        print(f"{self.__Name} attack {target.__Name} by {self.__Type}type skill!")
        if self.__Type == 'Electric' or self.__Type == 'Psychic' or self.__Type == 'Dragon':
            print("Super-effective!!")
            target.__Hp -= int(self.__Deal * 1.1)
        elif self.__Type == 'Grass':
            if target.__Type == 'Water':
                print("Super-effective!!")
                target.__Hp -= int(self.__Deal * 1.2)
            elif target.__Type == 'Fire':
                print("Not very effective...")
                target.__Hp -= int(self.__Deal / 1.2)
            else:
                target.__Hp -= self.__Deal
        elif self.__Type == 'Fire':
            if target.__Type == 'Grass':
                print("Super-effective!!")
                target.__Hp -= int(self.__Deal * 1.2)
            elif target.__Type == 'Water':
                print("Not very effective...")
                target.__Hp -= int(self.__Deal / 1.2)
            else:
                target.__Hp -= self.__Deal
        elif self.__Type == 'Water':
            if target.__Type == 'Fire':
                print("Super-effective!!")
                target.__Hp -= int(self.__Deal * 1.2)
            elif target.__Type == 'Grass':
                print("Not very effective...")
                target.__Hp -= int(self.__Deal / 1.2)
            else:
                target.__Hp -= self.__Deal