from cl_Unit import Unit
import random


class Knight(Unit):

    def Hit(self, other: Unit):
        if not isinstance(other, type(self)):
            raise TypeError

        if random.randint(0,1):
            self.Damage = self.Attack * 2 - other.Armor
        else:
            self.Damage = self.Attack - other.Armor

        print(f"Unit {self.Name} attacked {other.Name} on {self.Damage}")

        try:
            other.Health = other.Health - self.Damage
            return other.Health
        except ValueError:
            other.Health = 0
            return other.Health




