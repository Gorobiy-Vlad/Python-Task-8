class Unit:

    _Name = "-"
    _Health = 1
    _Attack = 1
    _Armor = 1

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, val: str):
        if not val.isalpha():
            raise TypeError
        self._Name = val

    @property
    def Health(self):
        return self._Health

    @Health.setter
    def Health(self, val):
        if val < 0:
            raise ValueError
        elif val == 0:
            print(f"Unit {self.Name} is dead (")
        self._Health = val


    @property
    def Attack(self):
        return self._Attack

    @Attack.setter
    def Attack(self, val):
        if val < 0:
            raise ValueError
        self._Attack = val

    @property
    def Armor(self):
        return self._Armor

    @Armor.setter
    def Armor(self, val):
        if val < 0:
            raise ValueError
        self._Armor = val

    def __init__(self, Name, Health, Attack, Armor):
        self.Name = Name
        self.Health = Health
        self.Attack = Attack
        self.Armor = Armor

    def __str__(self):
        print("*" * 100)
        return f"Information of unit {self.Name}:\n " \
               f"Health: {self.Health}\n " \
               f"Damage: {self.Attack}\n " \
               f"Armor: {self.Armor}"

    def Hit(self, other):
        if not isinstance(other, type(self)):
            raise TypeError

        Damage = self.Attack - other.Armor
        print(f"Unit {self.Name} attacked {other.Name} on {Damage}")
        try:
            other.Health = other.Health - Damage
            return other.Health
        except ValueError:
            other.Health = 0
            return other.Health
